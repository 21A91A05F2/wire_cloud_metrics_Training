# import requests
# from bs4 import BeautifulSoup

# url = "https://news.ycombinator.com/"

# response =  requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")




# #Extract headlines:

# headlines = soup.select(".titleline a")

# for index, headline in enumerate(headlines):
#     print(f"{index+1}. {headline.text} - {headline.get('href')}")


# # 1. The least amount of CSS for a decent looking site (2023) - https://thecascade.dev/article/least-amount-of-css/
# # 2. thecascade.dev - from?site=thecascade.dev
# # 3. Learning a foreign language–before you're born - https://nouvelles.umontreal.ca/en/article/2025/10/03/learning-a-foreign-language-before-you-re-born
# # 4. umontreal.ca - from?site=umontreal.ca
# # 5. Why did Crunchyroll's subtitles just get worse? - https://animebythenumbers.substack.com/p/worse-crunchyroll-subtitles
# # 6. animebythenumbers.substack.com - from?site=animebythenumbers.substack.com
# # 7. Apps SDK - https://developers.openai.com/apps-sdk/ 
# # 8. developers.openai.com - from?site=developers.openai.com
# # 9. Pdoc – Generate API documentation for Python projects - https://pdoc.dev/
# # 10. pdoc.dev - from?site=pdoc.dev
# # 11. Who owns Express VPN, Nord, Surfshark? VPN relationships explained (2024) - https://windscribe.com/blog/the-vpn-relationship-map/
# # 12. windscribe.com - from?site=windscribe.com
# # 13. Removing these 50 objects from orbit would cut danger from space junk in half - https://arstechnica.com/space/2025/10/everyone-but-china-has-pretty-much-stopped-littering-in-low-earth-orbit/
# # 14. arstechnica.com - from?site=arstechnica.com       
# # 15. Kirigami-inspired parachute falls on target - https://physicsworld.com/a/kirigami-inspired-parachute-falls-on-target/
# # 16. physicsworld.com - from?site=physicsworld.com     
# # 17. Using Deno as my game engine - https://explodi.tubatuba.net/2025/09/26/using-deno-as-my-game-engine     
# # 18. tubatuba.net - from?site=tubatuba.net
# # 19. Deloitte to refund the Australian government after using AI in $440k report - https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report
# # 20. theguardian.com - from?site=theguardian.com       
# # 21. No_color: Disabling ANSI color output by default - https://no-color.org/
# # 22. no-color.org - from?site=no-color.org
# # 23. OpenZL: An open source format-aware compression framework - https://engineering.fb.com/2025/10/06/developer-tools/openzl-open-source-format-aware-compression-framework/
# # 24. fb.com - from?site=fb.com
# # 25. Compiling a Forth - https://healeycodes.com/compiling-a-forth
# # 26. healeycodes.com - from?site=healeycodes.com       
# # 27. CodeMender: an AI agent for code security - https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/
# # 28. deepmind.google - from?site=deepmind.google       
# # 29. Origami Patterns Solve a Major Physics Riddle - https://www.quantamagazine.org/origami-patterns-solve-a-major-physics-riddle-20251006/
# # 30. quantamagazine.org - from?site=quantamagazine.org 
# # 31. Indefinite Backpack Travel - https://jeremymaluf.com/onebag/
# # 32. jeremymaluf.com - from?site=jeremymaluf.com       
# # 33. California law forces Netflix, Hulu to turn down ad volumes - https://www.politico.com/news/2025/10/06/dial-it-down-california-forces-netflix-hulu-to-lower-ad-volume-00595663
# # 34. politico.com - from?site=politico.com
# # 35. Mise: Monorepo Tasks - https://github.com/jdx/mise/discussions/6564
# # 36. github.com/jdx - from?site=github.com/jdx
# # 37. Microsoft is plugging more holes that let you use Windows 11 without MS account - https://www.twesomekling
# # wesomekling
# # wesomekling
# # 43. OpenAI ChatKit - https://github.com/openai/chatkit-js
# # 44. github.com/openai - from?site=github.com/openai
# # 45. Translating Cython to Mojo, a first attempt - https://fnands.com/blog/2025/sklearn-mojo-dbscan-inner/
# # 46. fnands.com - from?site=fnands.com
# # 47. It's just a virus, the E.R. told him – days later, he was dead - https://www.nytimes.com/2025/10/05/well/sam-terblanche-virus-death-columbia.html
# # 48. nytimes.com - from?site=nytimes.com
# # 49. How to tile matrix multiplication (2023) - https://alvinwan.com/how-to-tile-matrix-multiplication/
# # 50. alvinwan.com - from?site=alvinwan.com
# # 51. Ford CEO Says There Aren't Enough Mechanics. Then a Mechanic Responds - https://www.motor1.com/news/774805/ford-ceo-complains-shortage-mechanics/
# # 52. motor1.com - from?site=motor1.com
# # 53. RediShell: Critical remote code execution vulnerability in Redis - https://www.wiz.io/blog/wiz-research-redis-rce-cve-2025-49844
# # 54. wiz.io - from?site=wiz.io
# # 55. Radioactive Pottery and Glassware (2010) - https://carlwillis.wordpress.com/2010/01/12/nuclear-collection-part-iv/
# # 56. carlwillis.wordpress.com - from?site=carlwillis.wordpress.com
# # 57. Ghosts of Unix Past: a historical search for design patterns (2010) - https://lwn.net/Articles/411845/
# # 58. lwn.net - from?site=lwn.net
# # 59. Launch HN: Grapevine (YC S19) – A company GPT that actually works - https://getgrapevine.ai/ 
# # 60. getgrapevine.ai - from?site=getgrapevine.ai







# #we can save the extracted data for future use.

# import csv

# #open CSV file in write mode

# with open ("headlines.csv", "w", newline="", encoding= "utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow(["headline","Link"])

#     for headline in headlines:
#         writer.writerow([headline.text, headline.get("href")])

# print("Data saved to headlines.csv")


#Handling Websites with JavaScript:


from selenium import webdriver

driver = webdriver.Chrome()  #open chrome browser

driver.get("https://websitename.com") #open website

print(driver.title)  #print page title
driver.quit()  #Close brower







