import asyncio
import aiohttp
import nltk
import re
import csv, json
import async_timeout
import pandas as pd
from collections import Counter

def most_frequent(List):
    """Function for finding common tahoeIds"""
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

def remove_html(string):
    """Making string for comparison"""
    return re.sub('[^A-Za-z0-9]+', '', string)

def format_phonenumber(phonenumber):
    """Formating Phonenumbers"""
    phonenumber = phonenumber.replace("(", "")
    phonenumber = phonenumber.replace(")", "")
    phonenumber = phonenumber.replace("-", "")
    phonenumber = phonenumber.replace(" ", "")
    phonenumber = phonenumber.replace("[", "")
    phonenumber = phonenumber.replace("]", "")
    return int(phonenumber)

async def fetch_person(session, row):
    """This Function is Sending Person request"""
    try:
        
        async with async_timeout.timeout(10):
            try:         
                payload = json.dumps({
                    "FirstName": row[0],
                    "LastName": row[1],
                    "Addresses":[
                        {
                    "AddressLine2": row[-1]
                        }
                    ],
                    "ResultsPerPage": 1
                    })

                headers = {
                    'galaxy-ap-name': 'hawksrealestate',
                    'galaxy-ap-password': 'e1f7ed9a5bae4c398ea91e713c7e56a4',
                    'galaxy-search-type': 'Person',
                    'Content-Type': 'application/json'
                }
                try:
                    async with session.post("https://api.galaxysearchapi.com/PersonSearch", headers=headers, data=payload) as response:                        
                        return await response.json()
                except:
                    pass

            except Exception as e:
                import pdb;pdb.set_trace()
                print(row, str(e))
                return False
    except:
        import pdb;pdb.set_trace()
        pass

async def fetch_Business(session, row, payload):
    """This Function is Sending Business request"""
    try:
        
        async with async_timeout.timeout(10):
            try:         
                payload = json.dumps({
                    "BusinessName": row[1],
                    "AddressLine2": row[-1],
                    "ResultsPerPage": 1
                })

                headers = {
                    'galaxy-ap-name': 'hawksrealestate',
                    'galaxy-ap-password': 'e1f7ed9a5bae4c398ea91e713c7e56a4',
                    'galaxy-search-type': 'BusinessV2',
                    'Content-Type': 'application/json'
                }
                try:
                    async with session.post("https://api.galaxysearchapi.com/BusinessV2Search", headers=headers, data=payload) as response:                        
                        return await response.json()
                except:
                    pass

            except Exception as e:
                import pdb;pdb.set_trace()
                print(row, str(e))
                return False
    except:
        import pdb;pdb.set_trace()
        pass

async def write_person_result(result, row, writer):
    """This Function is writing person result Logic in SCENARIO 1"""
    if not result['isError']:
        print("not Error in fetching === {} -- {}".format(row[0], row[1]))
        persons_arr = result["persons"]
        
        for person in persons_arr:
            wireless_phone_numbers = []
            landline_phone_numbers = []
            
            for phonenumber in person["phoneNumbers"]:
                if phonenumber["phoneType"] == "Wireless":
                    if len(wireless_phone_numbers) < 4:
                        wireless_phone_numbers.append(format_phonenumber(phonenumber["phoneNumber"]))
                elif phonenumber["phoneType"] == "LandLine/Services":
                    if len(landline_phone_numbers) < 2:
                        landline_phone_numbers.append(format_phonenumber(phonenumber["phoneNumber"]))
            
            email_addresses = []
            for email_ad in person["emailAddresses"]:
                if len(email_addresses) < 3:
                    email_addresses.append(email_ad["emailAddress"])
            
            age = person.get("age", '')                                    

            for i in range(0, 4):
                try:
                    row.append(wireless_phone_numbers[i])
                except Exception as ex:
                    row.append("") 

            for i in range(0, 2):
                try:
                    row.append(landline_phone_numbers[i])
                except Exception as ex:
                    row.append("")         

            row.append(person["name"]["firstName"])
            row.append(person["name"]["lastName"])   
            indicators = person.get("indicators", '')
            row.append(age)
            for i in range(0, 3):
                try:
                    row.append(email_addresses[i])
                except Exception as ex:
                    row.append("") 
            writer.writerow(row)
            row.append(indicators.get('hasBankruptcyRecords', ''))
            row.append(indicators.get('hasBusinessRecords', ''))
            row.append(indicators.get('hasDivorceRecords', ''))
            row.append(indicators.get('hasDomainsRecords', ''))
            row.append(indicators.get('hasEvictionsRecords', ''))
            row.append(indicators.get('hasFeinRecords', ''))
            row.append(indicators.get('hasForeclosuresRecords', ''))
            row.append(indicators.get('hasJudgmentRecords', ''))
            row.append(indicators.get('hasLienRecords', ''))
            row.append(indicators.get('hasMarriageRecords', ''))
            row.append(indicators.get('hasProfessionalLicenseRecords', ''))
            row.append(indicators.get('hasPropertyRecords', ''))
            row.append(indicators.get('hasVehicleRegistrationsRecords', ''))
            row.append(indicators.get('hasWorkplaceRecords', ''))
            row.append(indicators.get('hasDeaRecords', ''))
            row.append(indicators.get('hasPropertyV2Records', ''))
            row.append(indicators.get('hasUccRecords', ''))
            row.append(indicators.get('hasUnbankedData', ''))
            row.append(indicators.get('hasMobilePhones', ''))
            row.append(indicators.get('hasLandLines', ''))
            row.append(indicators.get('hasEmails', ''))
            row.append(indicators.get('hasAddresses', ''))
            row.append(indicators.get('hasCurrentAddresses', ''))
            row.append(indicators.get('hasHistoricalAddresses', ''))
            row.append(indicators.get('hasDebtRecords', ''))            
    else:
        print("Error in fetching === {} -- {}".format(row[0], row[1]))

# async def write_business_result(result, row, writer):
    # """This function is writing business result Logic in SCENARIO 2"""
    # Bussiness_owner = []
    # tahoeId = []
    # if result['businessV2Records']:
    #     business_arr = result['businessV2Records']
    #     for business in business_arr:
    #         tahoeIds_list1 = []
    #         tahoeIds_list2 = []
    #         if business['usCorpFilings']:
    #             for crop in business['usCorpFilings']:
    #                 if remove_html(crop['name']).lower() == remove_html(row[1]).lower():
    #                     # import pdb;pdb.set_trace()
    #                     for tid_contacts in crop['contacts']:
    #                         tahoeIds_list1.append(tid_contacts['name']['tahoeId'])
    #                     if crop['officers']:
    #                         for tid_officers in crop['officers']:
    #                             tahoeIds_list2.append(tid_officers['name']['tahoeId'])    
    #                 tahoeIds_list1.extend(tahoeIds_list2)
    #             common = most_frequent(tahoeIds_list1)
    #             Bussiness_owner.append(str(row[1]))
    #             tahoeId.append(common)
    #         else:
    #             tahoeIds_list3 = []
    #             if business['newBusinessFilings']:
    #                 for nbf in business['newBusinessFilings']:
    #                     if remove_html(nbf['company']).lower() == remove_html(row[1]).lower():
    #                         for tid_contacts in nbf['contacts']:
    #                             tahoeIds_list3.append(tid_contacts['tahoeId'])
    # for Bussiness, tId in zip(Bussiness_owner, tahoeId):
    #     import pdb;pdb.set_trace()
    #     try:
    #         async with async_timeout.timeout(10):
    #             try:         
    #                 payload = json.dumps({
    #                     "LastName": Bussiness,
    #                     "TahoeID": tId,
    #                     "ResultsPerPage": 500
    #                 })
    #                 headers = {
    #                     'galaxy-ap-name': 'hawksrealestate',
    #                     'galaxy-ap-password': 'e1f7ed9a5bae4c398ea91e713c7e56a4',
    #                     'galaxy-search-type': 'Person',
    #                     'Content-Type': 'application/json'
    #                 }
    #                 try:
    #                     async with session.post("https://api.galaxysearchapi.com/PersonSearch", headers=headers, data=payload) as response:
    #                         return await response.json()
    #                 except:
    #                     pass

    #             except Exception as e:
    #                 import pdb;pdb.set_trace()
    #                 print(row, str(e))
    #                 return False
    #     except:
    #         import pdb;pdb.set_trace()
    #         pass
            

async def read_write_person_logic(session, row, writer):
    """This Function is fetching person result Logic for SCENARIO 1"""
    try:
        res = await fetch_person(session, row)    
        if res:
            await write_person_result(res, row, writer)
    except:
        import pdb;pdb.set_trace()
        print("")

async def read_write_business_logic(session, row, writer):
    """This Function is fetching business result Logic for SCENARIO 2"""
    try:
        payload = json.dumps({
                    "BusinessName": row[1],
                    "ResultsPerPage": 1
                    })
        result = await fetch_Business(session, row, payload)    
        if result:
        # """This function is writing business result Logic in SCENARIO 2"""
            Bussiness_owner = []
            tahoeId = []
            if result['businessV2Records']:
                business_arr = result['businessV2Records']
                for business in business_arr:
                    tahoeIds_list1 = []
                    tahoeIds_list2 = []
                    if business['usCorpFilings']:
                        for crop in business['usCorpFilings']:
                            if remove_html(crop['name']).lower() == remove_html(row[1]).lower():
                                # import pdb;pdb.set_trace()
                                for tid_contacts in crop['contacts']:
                                    tahoeIds_list1.append(tid_contacts['name']['tahoeId'])
                                if crop['officers']:
                                    for tid_officers in crop['officers']:
                                        tahoeIds_list2.append(tid_officers['name']['tahoeId'])    
                            tahoeIds_list1.extend(tahoeIds_list2)
                        common = most_frequent(tahoeIds_list1)
                        Bussiness_owner.append(str(row[1]))
                        tahoeId.append(common)
                    else:
                        tahoeIds_list3 = []
                        if business['newBusinessFilings']:
                            for nbf in business['newBusinessFilings']:
                                if remove_html(nbf['company']).lower() == remove_html(row[1]).lower():
                                    for tid_contacts in nbf['contacts']:
                                        tahoeIds_list3.append(tid_contacts['tahoeId'])
            for Bussiness, tId in zip(Bussiness_owner, tahoeId):
                # try:
                #     async with async_timeout.timeout(10):
                try:         
                    payload = json.dumps({
                        "LastName": Bussiness,
                        "TahoeID": tId,
                        "ResultsPerPage": 500
                    })
                    headers = {
                        'galaxy-ap-name': 'hawksrealestate',
                        'galaxy-ap-password': 'e1f7ed9a5bae4c398ea91e713c7e56a4',
                        'galaxy-search-type': 'Person',
                        'Content-Type': 'application/json'
                    }
                    try:
                        async with session.post("https://api.galaxysearchapi.com/PersonSearch", headers=headers, data=payload) as response:
                            import pdb;pdb.set_trace()
                            return await response.json()
                    except:
                        pass

                except Exception as e:
                    import pdb;pdb.set_trace()
                    print(row, str(e))
                    return False
                # except:
                #     import pdb;pdb.set_trace()
                #     pass
    except:
        # import pdb;pdb.set_trace()
        print("")

async def main():
    """Main Logic and NLTK work for seperate bussiness names"""
    async with aiohttp.ClientSession() as session:
        f = open('outputlogic1.csv', 'a', newline='')
        writer = csv.writer(f)
        data = ['First Name','Last Name','Property Address','Property City','Property State','Property Zip','Mailing Address','Mailing City','Mailing State','Mailing Zip','wireless1', 'wireless2', 'wireless3', 'wireless4', 'landline1', 'landline2', 'RecordFirstName', 'RecordLastName', 'Age', 'Email-1', 'Email-2', 'Email-3', 'BankruptcyRecords', 'BusinessRecords', 'DivorceRecords', 'DomainsRecords', 'EvictionsRecords', 'FeinRecords', 'ForeclosuresRecords', 'JudgmentRecords', 'LienRecords', 'MarriageRecords', 'ProfessionalLicenseRecords', 'PropertyRecords', 'VehicleRegistrationsRecords', 'WorkplaceRecords', 'DeaRecords', 'PropertyV2Records', 'UccRecords', 'UnbankedData', 'MobilePhones', 'LandLines', 'Emails', 'Addresses', 'CurrentAddresses', 'HistoricalAddresses', 'DebtRecords']
        writer.writerow(data)
        rows = pd.read_csv('realTestData.csv', delimiter=',')
        rows = [list(x) for x in rows.values]        
        person_records = []
        for row in rows:
            if len(str(row[0])) > 0:
                if str(row[1]) is not str(row[1]).lower().startswith(('sfr', 'bfr', 'srf', 'rs rental', 'rex', 'vb', 'bfs', 'bsf', 'conrex')) and (x for x in ['llc', ' lp', 'llp', 'lllp', 'ltd', 'inc', 'corp', ' ll ', ' l l c', 'l.l.c', 'l. l. c', 'limited liability company', 'limited partnership', 'enterprises', ' co '] if x not in str(row)):
                    if len(nltk.word_tokenize(row[1])) == 2:
                        firstName = nltk.word_tokenize(row[1])[0]
                        lastName = nltk.word_tokenize(row[1])[1]
                        row[0] = "{}".format(firstName)
                        row[1] = "{}".format(lastName)
                    elif len(nltk.word_tokenize(row[1])) > 2:
                        person_records.append(read_write_business_logic(session, row, writer))
                    # person_records.append(read_write_person_logic(session, row, writer))
     
        await asyncio.gather(*person_records)    
        print('!--- finished processing')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())