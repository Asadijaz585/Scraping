

from pkgutil import ImpImporter
import time
from sqlalchemy import create_engine
from  sqlalchemy.orm import scoped_session ,sessionmaker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def send_to_db():
    for url in cards:
        driver.get(url)
        time.sleep(3)
        engine = create_engine('mysql+pymysql://root@localhost/tcgplayer_records')
        db = scoped_session(sessionmaker(bind=engine))
        try:
            title = driver.find_element(By.XPATH,'//h1[@class="product-details__name"]').text
            price = driver.find_element(By.XPATH,'//div[@class="charts-price"]').text
            card_number = driver.find_element(By.XPATH,'//ul[@class="product__item-details__attributes"]/li[1]').text
            image = driver.find_element(By.XPATH,'//div[@class="VueCarousel-slide"]/div/span/div/img').get_attribute('src')
            sql = "INSERT INTO `card` (`title`,`price`,`card_number`,`image`,`urls`) VALUES ('{}','{}','{}','{}','{}')".format(title,price,card_number,image,url)
            db.execute(sql)
            db.commit()
            print("inserted")
            time.sleep(2)
        except:
            pass 




options = Options()
options.headless = True
profile = webdriver.FirefoxProfile()
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=profile, executable_path='geckodriver', options=options)
start_page = 1
set_url = [
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=2015-mega-tins-mega-pack%7Cduelist-league-promo",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=battle-pack-3-monster-league%7Cbattle-pack-epic-dawn",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=hidden-arsenal-chapter-1%7Clegendary-collection-3-yugis-world%7Clegendary-collection-4-joeys-world",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=legendary-collection-2%7C2019-gold-sarcophagus-tin-mega-pack%7Cdark-revelation-volume-1",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=dark-beginning-1%7Cdark-beginning-2%7C2020-tin-of-lost-memories%7C2014-mega-tins-mega-pack",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=dark-revelation-volume-4%7Cspeed-duel-battle-city-box%7Cspeed-duel-gx-duel-academy-box%7Cdragons-of-legend-the-complete-series",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=2016-mega-tins-mega-pack%7C2018-mega-tins-mega-pack%7Clegendary-duelists-season-2%7Cghosts-from-the-past-the-2nd-haunting",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=legendary-duelists-season-1%7Cmaximum-gold-el-dorado%7Clegendary-decks-ii%7Cking-of-games-yugis-legendary-decks%7Cghosts-from-the-past%7Cmagic-ruler",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=the-legend-of-blue-eyes-white-dragon%7Cthe-new-challengers%7Clegendary-hero-decks%7Clegendary-collection-kaiba%7Cstardust-overdrive%7Clegendary-dragon-decks%7Ccrossroads-of-chaos%7Clight-of-destruction",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=phantom-darkness%7Cra-yellow-mega-pack%7Cthe-duelist-genesis%7Cabsolute-powerforce%7Cancient-prophecy%7Ccrimson-crisis%7Cdark-legends%7Cabyss-rising",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=ancient-sanctuary%7Cduelist-revolution%7Cextreme-victory%7Cgalactic-overlord%7Cgeneration-force%7Clord-of-the-tachyon-galaxy%7Cphoton-shockwave%7Cprimal-origin",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=return-of-the-duelist%7Cstorm-of-ragnarok%7Cthe-shining-darkness%7Cdimension-of-chaos%7Cgladiators-assault%7Clegacy-of-the-valiant%7Cstarstrike-blast%7Cchaos-impact%7Cignition-assault",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=magicians-force%7Crising-rampage%7Cshadow-specters%7Cpharaonic-guardian%7Cbattle-of-chaos%7Cclash-of-rebellions%7Ccrossed-souls%7Cduelist-alliance%7Cjudgment-of-the-light",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=blazing-vortex%7Cburst-of-destiny%7Cdark-crisis%7Cdawn-of-majesty%7Cduel-overload%7Cduel-power%7Ceternity-code%7Clightning-overdrive%7Cphantom-rage",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=battles-of-legend-relentless-revenge%7Ccode-of-the-duelist%7Ccybernetic-horizon%7Cdark-neostorm%7Cflames-of-destruction%7Clabyrinth-of-nightmare%7Cmaximum-crisis%7Cpharaohs-servant%7Csavage-strike",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=soul-fusion%7Cspell-ruler%7Cbattle-pack-2-war-of-the-giants-%E2%80%93-round-2%7Clegacy-of-darkness%7Cbreakers-of-shadow%7Cinvasion-vengeance%7Craging-tempest",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=retro-pack-1%7Cshining-victories%7Cretro-pack-2%7Cthe-dark-illusion%7Cduel-terminal-1%7Cduel-terminal-2%7Cduel-terminal-3%7Cduel-terminal-4%7Cduel-terminal-5",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=duel-terminal-6%7Cduel-terminal-7%7Cduelist-saga%7Cpremium-gold-infinite-gold%7Cshonen-jump-magazine-promos%7Cstar-pack-2013%7Cstar-pack-2014%7Cstar-pack-battle-royal%7Cstar-pack-vrains%7Cstar-pack-arc-v",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=force-of-the-breaker%7Cbrothers-of-legend%7Cbattles-of-legend-armageddon%7Cbattles-of-legend-heros-revenge%7Cshadow-of-infinity%7Celemental-energy%7Cpremium-gold-return-of-the-bling%7Cpremium-gold%7Cthe-lost-millennium%7Ccyberdark-impact",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=cybernetic-revolution%7Cenemy-of-justice%7Cflaming-eternity%7Cpower-of-the-duelist%7Crise-of-destiny%7Csoul-of-the-duelist%7Ckings-court%7Cbattles-of-legend-lights-revenge%7Cancient-guardians%7Cgenesis-impact%7Cthe-grand-creators%7Ctoon-chaos",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=dragons-of-legend-unleashed%7Chidden-arsenal-7-knight-of-stars%7Cspeed-duel-decks-duelists-of-tomorrow%7Cspeed-duel-decks-match-of-the-millennium%7Cyu-gi-oh-tokens%7Cspeed-duel-decks-twisted-nightmares%7Cspeed-duel-decks-destiny-masters%7Cspeed-duel-decks-ultimate-predators%7Cthe-dark-side-of-dimensions-movie-pack-gold-edition%7Cthe-dark-side-of-dimensions-movie-pack-secret-edition%7Chidden-arsenal-4%7Chidden-arsenal-5-steelswarm-invasion%7Cspeed-duel-trials-of-the-kingdom%7Cdark-saviors%7Cdestiny-soldiers", 
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=fists-of-the-gadgets%7Cfusion-enforcers%7Chidden-arsenal-2%7Chidden-arsenal-4%7Chidden-arsenal-3%7Chidden-arsenal-6-omega-xyz%7Chidden-summoners%7Chigh-speed-riders%7Cmystic-fighters%7Cnumber-hunters%7Cpendulum-evolution%7Csecret-slayers%7Cshadows-in-valhalla%7Cspirit-warriors%7Cthe-infinity-chasers%7Cthe-secret-forces",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=wing-raiders%7Clegendary-duelists-immortal-destiny%7Clegendary-duelists-rage-of-ra%7Clegendary-duelists-synchro-storm%7Cthe-dark-side-of-dimensions-movie-pack%7Cduel-devastator%7Clegendary-duelists-magical-hero%7Clegendary-duelists-sisters-of-the-rose%7Clegendary-duelists-white-dragon-abyss%7Cgold-series-haunted-mine%7Clegendary-duelists-ancient-millennium%7Clegendary-duelists%7Cworld-superstars%7Cdragons-of-legend%7Cstarter-deck-yugi%7Cstructure-deck-albaz-strike%7Cgold-series-2009%7Cgold-series-3",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=gold-series-4-pyramids-edition%7Cspeed-duel-arena-of-lost-souls%7Cspeed-duel-attack-from-the-deep%7Cstarter-deck-joey%7Cstarter-deck-kaiba%7Cstarter-deck-kaiba-evolution%7Cstarter-deck-pegasus%7Cstarter-deck-yugi-evolution%7Cstructure-deck-spirit-charmers%7Cstarter-deck-kaiba-reloaded%7Cstructure-deck-shaddoll-showdown%7Cmillennium-pack%7Cstructure-deck-cyber-strike%7Cstructure-deck-sacred-beasts%7Cduelist-pack-battle-city%7Cstarter-deck-yugi-reloaded%7C5ds-2008-starter-deck%7Cduelist-pack-rivals-of-the-pharaoh%7Cstructure-deck-freezing-chains%7Cstructure-deck-rokket-revolt",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=dragons-of-legend-2%7Cduelist-pack-dimensional-guardians%7Cgold-series-2008%7Cstarter-deck-codebreaker%7Cstructure-deck-hero-strike%7Cstructure-deck-soulburner%7Cstructure-deck-yugi-muto%7Cnoble-knights-of-the-round-table-box-set%7Cstructure-deck-seto-kaiba%7Cthe-lost-art-promotion%7C5ds-starter-deck-2009%7Cstarter-deck-dawn-of-the-xyz%7Cstarter-deck-link-strike%7Cstarter-deck-xyz-symphony%7Cstarter-deck-yuya%7Cstructure-deck-cyberse-link%7Cstructure-deck-master-of-pendulum%7Cstructure-deck-pendulum-domination%7Cstructure-deck-synchron-extreme%7Cstarter-deck-duelist-toolbox%7Cstructure-deck-emperor-of-darkness%7Cstructure-deck-lair-of-darkness",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=structure-deck-powercode-link%7Cstructure-deck-rise-of-the-true-dragons%7Cstructure-deck-wave-of-light%7Cstructure-deck-zombie-horde%7Csuper-starter-v-for-victory%7Cstarter-deck-syrus-truesdale%7Cstructure-deck-mechanized-madness%7Cstructure-deck-order-of-the-spellcasters%7Cstructure-deck-samurai-warlords%7Cduelist-pack-kaiba%7Cstructure-deck-dinosmashers-fury%7Cstructure-deck-dragons-collide%7Cstructure-deck-machine-reactor%7Cstructure-deck-saga-of-blue-eyes-white-dragon%7Csuper-starter-space-time-showdown%7Cstructure-deck-cyber-dragon-revolution%7Cstructure-deck-dragunity-legion%7Cstructure-deck-gates-of-the-underworld%7Cstructure-deck-onslaught-of-the-fire-kings%7Cstructure-deck-realm-of-the-sea-emperor%7Cstructure-deck-spellcasters-command%7Cegyptian-god-deck-slifer-the-sky-dragon%7Cstructure-deck-lost-sanctuary%7Cstructure-deck-marik",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=structure-deck-machina-mayhem%7Cstructure-deck-machine-re-volt%7Cstructure-deck-rise-of-the-dragon-lords%7Cstructure-deck-zombie-world%7Cyu-gi-oh-video-game-promotional-cards%7Cstructure-deck-realm-of-light%7Cstructure-deck-spellcasters-judgment%7Cstructure-deck-the-dark-emperor%7Cstructure-deck-warriors-triumph%7Cegyptian-god-deck-obelisk-the-tormentor%7Cspeed-duel-tournament-pack-3%7Cstructure-deck-geargia-rampage%7Cstructure-deck-fury-from-the-deep%7Cstructure-deck-invincible-fortress%7Cduel-terminal-preview%7Cstructure-deck-blaze-of-destruction%7Cduelist-pack-10-yusei-3%7Cduelist-pack-11-crow%7Cduelist-pack-1-jaden-yuki%7Cduelist-pack-2-chazz-princeton%7Cduelist-pack-3-jaden-yuki-2%7Cduelist-pack-4-zane-truesdale%7Cduelist-pack-5-aster-phoenix%7Cduelist-pack-8-yusei-fudo%7Cduelist-pack-9-yusei-2%7Cduelist-pack-yugi%7Chidden-arsenal%7Cpremium-pack-2%7Ctournament-pack-1%7Ctournament-pack-2",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=structure-deck-dragons-roar%7Cstructure-deck-zombie-madness%7Castral-pack-7%7Castral-pack-8%7Cots-tournament-pack-1%7Cots-tournament-pack-2%7Cots-tournament-pack-3%7Cots-tournament-pack-4%7Cots-tournament-pack-5%7Castral-pack-3%7Castral-pack-4%7Castral-pack-5%7Cots-tournament-pack-15%7Cots-tournament-pack-14%7Cots-tournament-pack-12%7Cots-tournament-pack-18%7Cots-tournament-pack-6%7Cots-tournament-pack-10%7Cots-tournament-pack-13%7Cots-tournament-pack-16%7Cots-tournament-pack-11%7Cots-tournament-pack-17%7Cots-tournament-pack-7%7Cots-tournament-pack-8%7C2010-collectors-tins%7C2012-premium-collection-tin%7Castral-pack-1%7Castral-pack-2%7Cduelist-pack-6-jaden-yuki-3%7Cduelist-pack-7-jesse-anderson%7C2013-zexal-collection-tin%7Cadvent-calendar-2011-adventskalender%7Cadvent-calendar-2018%7Cadvent-calendar-2019%7Cyu-gi-oh-championship-series-prize-cards%7C2012-collectors-tin%7Cjudge-promotional-cards%7Cmcdonalds-promo-series-2%7Cpremium-pack-1",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=duelist-pack-special-edition%7Cthe-falsebound-kingdom%7Cnintendo-ds-nightmare-of-troubadour%7Cyu-gi-oh-5ds-tag-force-promotional-cards%7Cthe-dark-illusion-special-edition-eu%7C2011-duelist-pack-tin%7Cyu-gi-oh-r-manga-promo%7Cgx-duel-academy-gba-promo%7C2004-collectors-tin%7Chobby-league-3%7Cpower-of-chaos-yugi-the-destiny%7Cdestiny-board-traveler-promo%7Csuper-starter-v-for-victory-power-up-pack%7Cgx-ultimate-beginners-pack-1%7Cforbidden-legacy%7C2010-duelist-pack-collection-tin%7Csamurai-assault%7Cyu-gi-oh-movie-exclusive-pack%7Credemption-replacement%7Cmcdonalds-promo%7Cduelist-revolution-se%7Cps2-yugioh-gx-the-beginning-of-destiny%7Cabyss-rising-se%7Cdawn-of-destiny-xbox%7Cbreakers-of-shadow-special-edition%7Ctournament-pack-6%7Cmattel-action-figure-promos-series-1%7Cworld-championship-series%7Celemental-hero-collection-2%7Cyu-gi-oh-day-promos%7Cfire-fists-special-editon%7Cyu-gi-oh-gx-tag-force-promotional-cards%7Cyu-gi-oh-zexal-world-duel-carnival-promos%7Cworld-championship-2006-ultimate-masters%7Ctournament-pack-7%7Cworld-championship-2004-gba-promo%7Cpharaoh-tour-promos%7Cyu-gi-oh-5ds-manga-promotional-cards%7Cspeed-duel-demo-deck%7C2016-mega-tins%7C2018-mega-tins%7Cchampion-pack-3%7Chobby-league-7%7Cjudgment-of-the-light-deluxe-edition%7Ccrossed-souls-advanced-edition%7Cadvanced-demo-deck-extra-pack%7Camerican-god-cards%7Cduel-masters-guide%7C2006-collectors-tin%7Cclash-of-rebellions-special-edition%7Ctoys-r-us-throwdown-promo%7Chobby-league-1%7Cevent-pack-speed-duel%7C2005-collectors-tin%7Cinvasion-vengeance-special-edition%7Cdemo-deck-2016%7Cyu-gi-oh-gx-manga-promotional-cards%7Cyu-gi-oh-zexal-manga-promotional-cards%7Cabsolute-powerforce-special-edition%7Csneak-preview-series-3%7Cchampion-pack-1%7Cspeed-duel-tournament-pack-1%7Craging-tempest-special-edition%7Celemental-hero-collection-1%7C2019-gold-sarcophagus-tin%7Chobby-league-4%7Cyu-gi-oh-5ds-over-the-nexus-promo-cards%7Clegendary-collection-1%7Cyu-gi-oh-gx-tag-force-evolution-promo%7C2009-collectors-tin%7Cchampion-pack-2%7Ctournament-pack-4%7Cshonen-jump-championship-series-promos%7Cgx-next-generation-blister-pack-promo%7Cyu-gi-oh-arc-v-promo-cards%7Ctactical-evolution-special-edition%7Cspeed-duel-tournament-pack-2%7Cgx-tag-force-promo%7Cmattel-action-figure-promos-series-3%7Cstructure-deck-deluxe-edition%7Cshonen-jump-championship-series-prize-cards%7Cstorm-of-ragnarok-se%7Ctournament-pack-3%7Cdemo-deck-2015%7Cturbo-pack-booster-five%7Cdemo-pack%7Cchampion-pack-6%7Cchampion-pack-8%7Cancient-prophecy-se%7Cchampion-pack-4%7Cchampion-pack-5%7Csneak-preview-series-4%7Cgeneration-force-se%7Ccosmo-blazer-se%7Cyu-gi-oh-the-movie-ani-manga-promo%7Cx-saber-power-up%7Cworld-championship-2008%7C2008-collectors-tin%7C2015-mega-tins%7C2014-mega-tins%7C2017-mega-tins%7Cworld-championship-2008-ds-game%7Cultimate-edition-2%7Ctwilight-edition%7Cthe-valuable-book-volume-5%7Csneak-preview-series-5%7Cyu-gi-oh-5ds-wheelie-breakers-promotional-cards%7Creverse-of-arcadia-promos%7Cturbo-pack-booster-three%7Chobby-league-6%7C2002-collectors-tin%7Canniversary-pack%7Cturbo-pack-booster-four%7Cturbo-pack-booster-six%7Cturbo-pack-booster-two%7Ctournament-pack-5%7Ctournament-pack-8%7Cworld-championship-2011-card-pack%7C2011-collectors-tins",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=legendary-collection-5ds%7C2021-tin-of-ancient-battles%7C2015-mega-tins-mega-pack",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=dark-revelation-volume-3%7Cdark-revelation-volume-2%7C2017-mega-tins-mega-pack%7Cmaximum-gold",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=metal-raiders%7Csecrets-of-eternity%7Cmagic-ruler%7Cinvasion-of-chaos%7Corder-of-chaos%7Ccosmo-blazer%7Craging-battle%7Ctactical-evolution",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=rise-of-the-duelist%7Ccircuit-break%7Cextreme-force%7Cstrike-of-neos%7Cspeed-duel-scars-of-battle%7Cstarter-deck-2006%7Cstarter-deck-jaden-yuki%7Cstructure-deck-warriors-strike%7Cstructure-deck-dinosaurs-rage%7Cstructure-deck-lord-of-the-storm%7Cstarter-deck-dark-legion%7Castral-pack-6%7Cots-tournament-pack-9%7Cstarter-deck-saber-force",
    "https://www.tcgplayer.com/search/yugioh/product?productLineName=yugioh&page={start}&view=grid&ProductTypeName=Cards&setName=turbo-pack-booster-one-pack%7Cturbo-pack-booster-eight%7Cturbo-pack-booster-seven%7Cbattle-pack-tournament-prize-cards%7C2013-collectors-tins%7Chobby-league-2%7Cstairway-to-the-destined-duel%7Cyu-gi-oh-5ds-reverse-of-arcadia-promo%7Cduelist-of-the-roses%7Cworld-championship-2007%7Cyu-gi-oh-value-boxes%7Chobby-league-5%7Csneak-preview-series-2%7Cthe-dark-side-of-dimensions-movie-pack-special-edition%7Ceternal-duelist-soul%7Cgladiators-assault-se%7Cgx-spirit-caller-promo%7Cworld-championship-2005-7-trials-to-glory%7Cchampion-pack-7%7Craging-battle-se%7Ccollectors-boxes%7C2007-collectors-tin%7Cworld-championship-2010-card-pack"    
]

time.sleep(3)

def get_links(driver):
    elems = driver.find_elements(By.XPATH,'//div[@class="search-result__content"]/a')
    time.sleep(2)
    return [elem.get_attribute('href') for elem in elems]
 
cards = []
for set in set_url:
    driver.get(set.format(start=start_page))
    time.sleep(4)
    cards.extend(get_links(driver))
    time.sleep(3)
    while start_page < 1200:
        start_page += 1
        driver.get(set.format(start=start_page))
        time.sleep(4)
        cards.extend(get_links(driver))
        time.sleep(3)
    total_pages = int(driver.find_element(By.XPATH, '//div[@class="results"]').text.split("of ")[1].split(" ")[0])
    print(total_pages)        
# for i in range(1, total_pages+1):
#     print("next page to {}".format(i))

send_to_db()
    
            
