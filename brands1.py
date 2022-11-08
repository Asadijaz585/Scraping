
import re, os, time, math, requests, json, csv
from requests.structures import CaseInsensitiveDict
def set_price_format(price):
    if "$" in price:
        return price
    return "${}0".format(price)


def download_images(data):
    url = data[len(data)-4]
    try:
        if 'list' in str(type(url)):
            url = data[len(data)-3]
        img_name =  url.split("sku/")[1]
        img_name = img_name.split("?")[0]
        url_1 = url.split("sku/")[::-1][1]
        img_name_1 = str(url_1)+'sku/'+str(img_name)
        # print(img_name)
        # print(img_name_1)
        cookies = dict(BCPermissionLevel='PERSONAL')
        with open('images/{}'.format(img_name), 'wb') as handle:
            print("Download Images function")
            response = requests.get(img_name_1, headers={"User-Agent": "Mozilla/5.0"}, cookies=cookies,stream=True)
            if not response.ok:
                response = requests.get(img_name_1, headers={"User-Agent": "Mozilla/5.0"}, cookies=cookies,stream=True)
                if not response.ok:
                    response = requests.get(img_name_1, headers={"User-Agent": "Mozilla/5.0"}, cookies=cookies,stream=True)
                img_name =  data[len(data)-2].split("sku/")[1]
                os.remove('images/{}'.format(img_name))
                url = data[len(data)-2]
                img_name =  url.split("sku/")[1]
                with open('images/{}'.format(img_name), 'wb') as handle:
                    response = requests.get(img_name_1, headers={"User-Agent": "Mozilla/5.0"}, cookies=cookies,stream=True)
                    print (response)
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
    except Exception as ex:
        print("Bad Url Found")
        with open('badurl.json', 'a') as f:
         json.dump(url, f, indent=2)
regex = re.compile(r'<[^>]+>')

def remove_html(string):
    return regex.sub('', string)

def get_recommendations(url):
    passkey = "caQ0pQXZTqFVYA1yYnnJ9emgUiW59DXA85Kxry8Ma02HE"
    product_id = url.split("?")[0].split("-")[-1]
    api_url = "https://api.bazaarvoice.com/data/reviews.json?Filter=contentlocale%3Aen*&Filter=ProductId%3A{}&Sort=SubmissionTime%3Adesc&Limit=6&Offset=0&Include=Products%2CComments&Stats=Reviews&passkey={}&apiversion=5.4&Locale=en_US".format(product_id, passkey)
    headers = CaseInsensitiveDict()
    headers["Accept"] = "*/*"
    headers["Accept-Language"] = "en-US,en;q=0.9"
    headers["Connection"] = "keep-alive"
    headers["Origin"] = "https://www.sephora.com"
    headers["Referer"] = "https://www.sephora.com/"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Site"] = "cross-site"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    resp = requests.get(api_url, headers=headers)
    try:
        resp = json.loads(resp.text)["Includes"]["Products"]
        key = list(resp.keys())[0]
        resp = resp[key]["ReviewStatistics"]
        recommended = resp["RecommendedCount"]
        total_reviews = resp["TotalReviewCount"]
        result = math.ceil((recommended/total_reviews)*100)
    except Exception as ex:
        result = "N/A"
    return result
f = open('1.csv', 'a+', encoding='UTF8', newline='')
header = ['Category', 'Sub-Category', 'Product Type', 'Brand', 'Product Name', 'Color', 'Color Description', 'Size', 'Price', 'Highlights', 'About The Product', 'Ingredients', 'How To Use', 'SKU ID', 'Review Score', 'No. Of Reviews', '% Recommend', 'URL', 'Product Photo 1 URL', 'Product Photo 2 URL', 'Color Photo URL']
writer = csv.writer(f)
writer.writerow(header)
with open('g.json') as f:
    urls = json.load(f)


for url in urls:
    try:
        cookies = dict(BCPermissionLevel='PERSONAL')
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, cookies=cookies,stream=True)
        data = json.loads(response.text.split("linkStore")[1].split(
                "</script")[0].replace('" type="text/json" data-comp="PageJSON ">', ''))["page"]["product"]            
                # except Exception as e:
                #     with open('badurl1.json', 'w') as f:
                #         json.dump(url, f, indent=2)
        # import pdb;pdb.set_trace()
        category_ref = json.loads(data["breadcrumbsSeoJsonLd"])["itemListElement"]
        # print(category_ref)
        category = category_ref[0]["item"]["name"]
        sub_category = category_ref[1]["item"]["name"]
        product_type = ""
        if len(category_ref) > 2:
            product_type = category_ref[2]["item"]["name"]
        product_other_images = []
        if "alternateImages" in data["currentSku"]:
            for img in data["currentSku"]["alternateImages"]:
                for i in range(1):
                    product_other_images.append(
                        "https://www.sephora.com{}".format(img["imageUrl"]))
                    i
                    break
                break
            product_other_images = []
            if "imageUrl" not in data["currentSku"].keys():
                product_other_images.append('N/A')
        brand_name = data["productDetails"]["brand"]["displayName"]
        product_ingredient = ""
        if "ingredientDesc" in data["currentSku"].keys():
            product_ingredient = remove_html(data["currentSku"]["ingredientDesc"])
        highlights = ""
        if "highlights" in data["currentSku"].keys():
            for highlight in data["currentSku"]["highlights"]:
                highlights += highlight["altText"].strip() + ";"
        how_to_use = remove_html(data["productDetails"]["suggestedUsage"])
        product_about = remove_html(data["productDetails"]["longDescription"])
        product_name = data["productDetails"]["displayName"]
        product_review_score = ""
        if "rating" in data["productDetails"].keys():
            product_review_score = data["productDetails"]["rating"]
        product_no_of_reviews = ""
        if "reviews" in data["productDetails"].keys():
            product_no_of_reviews = data["productDetails"]["reviews"]
        recommendations = get_recommendations(url)
        if "regularChildSkus" in data.keys():
            for color in data["regularChildSkus"]:
                size = color.get("size", "")
                color_description = color.get("variationDesc", "")
                color_name = ""
                if color.get("variationType", "") != "Size":
                    color_name = color.get("variationValue", "")
                if len(product_other_images) > 1:
                    if "smallImage" in color.keys():
                        try:
                            data = [
                                category, sub_category, product_type, brand_name, product_name, color_name, color_description, size, set_price_format(color["listPrice"]), highlights, product_about, product_ingredient,
                                how_to_use, color.get("skuId" ""), product_review_score, product_no_of_reviews, recommendations, "https://www.sephora.com{}".format(color["targetUrl"]), "https://www.sephora.com{}".format(color["skuImages"]["imageUrl"]),
                                product_other_images,
                                "https://www.sephora.com/productimages/sku/s{}-av-02-zoom.jpg".format(color["skuId"]),
                                "https://www.sephora.com{}".format(color["smallImage"])
                            ]
                        except Exception as ex:
                            print(ex)
                            import pdb;pdb.set_trace()
                            print("")
                    else:
                        data = [
                            category, sub_category, product_type, brand_name, product_name, color["variationValue"], color_description, size, set_price_format(color["listPrice"]), highlights, product_about, product_ingredient,
                            how_to_use, color["skuId"], product_review_score, product_no_of_reviews, recommendations, "https://www.sephora.com{}".format(color["targetUrl"]), "https://www.sephora.com{}".format(color["skuImages"]["imageUrl"]),
                            product_other_images,
                            "https://www.sephora.com/productimages/sku/s{}-av-02-zoom.jpg".format(color["skuId"]),
                            ""
                        ]
                else:
                    color_name = ""
                    if color.get("variationType", "") != "Size":
                        color_name = color.get("variationValue", "")
                    if "smallImage" in color.keys():
                        data = [
                            category, sub_category, product_type, brand_name, product_name, color_name, color_description, size, set_price_format(color["listPrice"]), highlights, product_about, product_ingredient,
                            how_to_use, color["skuId"], product_review_score, product_no_of_reviews, recommendations, "https://www.sephora.com{}".format(color["targetUrl"]), "https://www.sephora.com{}".format(color["skuImages"]["imageUrl"]),
                            product_other_images,
                            "",
                            "https://www.sephora.com{}".format(color["smallImage"])
                        ]
                    else:
                        data = [
                            category, sub_category, product_type, brand_name, product_name, color_name, color_description, size, set_price_format(color["listPrice"]), highlights, product_about, product_ingredient,
                            how_to_use, color["skuId"], product_review_score, product_no_of_reviews, recommendations, "https://www.sephora.com{}".format(color["targetUrl"]), "https://www.sephora.com{}".format(color["skuImages"]["imageUrl"]),
                            product_other_images,
                            "",
                            ""
                        ]
                # download_images(data)
                writer.writerow(data)
        else:
            data = json.loads(data["productSeoJsonLd"])
            data = [
                category,
                sub_category,
                product_type,
                brand_name,
                product_name,
                "",
                "",
                "",
                set_price_format(data["offers"][0]["price"]),
                highlights,
                product_about,
                product_ingredient,
                how_to_use,
                data["offers"][0]["sku"],
                product_review_score,
                product_no_of_reviews,
                recommendations,
                url,
                product_other_images,
                "{}".format(data["offers"][0]["image"]),
                "https://www.sephora.com/productimages/sku/s{}-av-02-zoom.jpg".format(data["offers"][0]["sku"]),
                ""
            ]
            # download_images(data)
            writer.writerow(data)
    # except Exception as ex:
    #     with open('badurl2.json', 'a') as f:
    #      json.dump(url, f, indent=2)
    except KeyError:
        pass

print("DONE")