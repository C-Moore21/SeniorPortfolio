# This code is defunct and no longer used per suggestion by an BLM employee
# that the data being scraped here is 'unrealiable' and not used in production code.

# import libraries
from bs4 import BeautifulSoup
import requests

status_list = ["Analysis & Document Preparation", "Comment+and+Review+Period", "Decision and Appeal",
               "Decision and Protest", "Final EIS (non LUP)", "PRMP - Protest and Resolution", "Preparation and Planning", "Public Scoping"]

status_list_form_info = ["7-fvcrIA0xl6OPzHlZrOBB-F4KmqIduGWVHChIboWIGU3ovsQbwkXnPsfGVEhlPsjWS0BryebS3qMp88EJTqXvrJLu4NOipmTLTEGMicA51OvvpKvdLOeiliQDJ5DRo7qAe1XKeXOBlaFVFQSNMaWh8GZzYGHJGRzlxuClr5y9I=",
                         "h3YdK_DlT_iAZko3JTYgBEE2xYe4VGFQRzd1RRjBqGEZKEdBqeOgU7G60xHKIgm9kCvfbWkrcHaPIAem-3TLLh_jvWksYHQOi9gPnL1O8sJpFUrHE01WYt7Tq4LOfQUBRcVGxKtJzSE4JZlDGCN3G-X06mzo3Hc8kiT_G5H3T9rgj5EfM5i0tCy4XBN6Z2x9FTPFvMyMuIb_0V8pkpFWej8rjgFLRb6KP19sFtyFMKDEXE1oS_kLdfVdjtLpIm4Rv8sEjNZJEpGM24cObPOfweOtXs_wrnFpYfWkkhMuhAAwOOaNbmhBepJBtrVJUhN3z-b8x9F_wfBR6GHAMgLGwv8ZNdevxnNOdLPGRohq0cD6uuRT3l-OVJH7JVRlJTMYRsB2mPf4uQokUy3HuRPrWrwPbOAHJUKCLIRYUksxO8nl0FMXPKq51uh4DI1QrUHi3AmArMzWcJc=",
                         "YqZYO6ybLr5SXcMs5o5aLsW8AxetkQRti6DF7FBtyos5TnoCohiXPxAjLR6SF6ZyvKnF2yRFUcoPeHzYC4YVJKilnojGp6XKtoEOY9tlkEgmCt3Av1rFDdblYWo7gvgT5d4WsGEwCivod-cOW1bSL2teWcopNVO4kFVgd4qGkVc=",
                         "zQwBaEJ7hwfddvvRzG0nInnb38Tv5jkDED5rIQaGwfeyV8cRuKft0QH7MTcpsS8vT6p1m8McSNyrd2n2COAHW9N0lPMteieQNWaV2hbgx-3x0LSgTrAR2QijfyYc1Y5axG7EQmIQBVtjgrQKK0rgFLw95Za2s60a1tj4N7NdWZ3Ql7qhIBmtTl6PUMR5RurWz54hdGUxMXXCZE7vGRyfIcOYRkYUOMoCBFkrLWA5FAfiO3eVyctysqn-uA28h_Uhc-YrwTrGIOT53J59FmuJxT87bPU9vDXGRPPEr-eEtgqFOt5iYf2oesKlcX3fNeN6SK6SC9Um0FfOv-BTR-p2OyJjUygKKxQbuqKiglZr-mbuBr-pIs5MIyKuk4XXpu7OYuEBRXuTEfE8REMwsOwL0EG5qN525SB_lWLTmDkCezftMCxVlcOtboLFRsXTNGODYSmgaLBqmjU=",
                         "8s8-vzdfeiQhce_Mk8vOVLUNWtKKOJug9DB7YwxErSHgMa8741ddb6L5CJVEoEo_9p-X-j8T9-Hgu35RWl8tbnG8LirWUS8jAbkTuciAiHfxNeRrQLCJbLHtSp6D4HQV9rNdo9ZaWMJjanqx21HjfGFC4rVxvpazbK2ETqtvN5aqoy2xHaom8WndJBBEfg31SMsx8uEpglzEkI-FPlbcobRYbHakuEJ2yGFVjEVVaG2_zf8v5tM5YIMDSqhnxgaN7eB-vJnL2ETVZzbQkLExFS1798bBXCjAN44AJGjFMi6hEO4svT3sfbhLsIk8Wc2L8tYnfmSMQQqwWY1BLtuJpauXpTSwz4Y4LGzltnvhLo2_vTF4Gk8z8OKVdMNFRoV-PZuPnTwn8BULjVyxaeCvPQnLsutN8_rleGjlubMZQR_hV3eibJ4EeUrDuPghTPqDNP_CULwE4zw=",
                         "TDmj3yiklOGOWU_j33mnBvhkhQCxtT919chywm9m8lmHFcavA2dAkgPvm_uMLxM8Fpqd0PKS1585MJWRKTS-XeC0rvhlECgkR1Bhtn5qooC4RZwjnHvDDv56UDZ1gsBwL8CrehydvJS_F1fcsJUhnfLQHcqpsZz4IAR2gX2bRUL438n6KQqY59jXfyWYDtQNGIcr3HbD2oEjtgTw1T4H49-LayqM_7eXRbt1P-mWy-IzHnaQz_o9e1BcQB_l5UoQ_5Z0Sw42MhO9M0xBKJUAw13VUpmXrc_6annr1VHxTncVwgU9KQou2pYVx37MV83waSKCCOwkW2OYPmSCox1BcvEPi4BRLYTL8dG4SB4BwL57DMlMZl1tTVq3HyVOI-lp",
                         "4gXWS38I0m2r37jwv27pAhVvxLWFL41xvBhHLfplIcVrtda8gi0MKgRgK-V7uY0oR1SYI2y-57yr4P3nq7F1qlrse_wGp1-Jkue5N2zwWh_Zo6TnKWd30cvg95ge4UMLVQeZYoKZbpO1LGTQJ_3hJ6tIELwMqB-Atj49hCS-nKXqbYUHuyXmi_RcL4NLA7aQni8BV9Q2NwrkH8EblTlGujAQBeold1VTX8n827EU2Gphb84gxvmCpwGz5BEK91OeqE8d33yr12NPzPLKLKXi7IJQNP-oDffrS3xiZOtHS77jwTVJcBO2-eKLt_s3iQ2C0F5pXtDvat2FFgCtaX_SPHno05IZOeE0bGWBkyd-ohqeThKD-I6-XFvsXWVZIXdjbaOklH4mme0y_8FIPuMmpq33T_fpPGsyKWqrAOGPW8ED_QMtq9hmQ_23vJM5I031T1RJ1S-cBOg=",
                         "jwDVnDeOItJj_OxmPWeF9vg4wu6NoEcFh-ZrUa4S2tNiT0fF-b2xrz6AJNdEq4Oxcrxh85b0Vyumv_4pEaeXcAtPV9MhVfdqLwbF8x7v2UeOe1wYbqDBDsTFWmCaPkDueGzmHjy0ulgQo-7g298tEYpG8fQDWaaD8yoz9QShx1A="
                         ]

# status_list = ["Preparation and Planning"]
for status, form_info in zip(status_list, status_list_form_info):
    headers = {
        'Host': 'eplanning.blm.gov',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',

        'Referer': 'https://eplanning.blm.gov/epl-front-office/eplanning/nepa/nepa_register.do',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '1042',
        'Cookie': 'JSESSIONID=22CA434D2031983379AF5C55CEA23198; BNES_JSESSIONID=obXatqFBmfADRZZRaUkMf4nIdoCDZB+2C9tqoX6Gkd44OMKvY4H6Kc2SoLAHYC5WssJIlUTzvcS2FgAMWWl2U19S8FCPdZN/9wHjWs7jQOjliuPV90eZLg==',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    payload = {'method': '',
               'jumpTo': '',
               'sortBy': '',
               'searchType': 'advanced',
               'selectedOfficeList': 'all',
               'selectedCountyList': 'all',
               'nepaOrLup': 'true',
               'group1': 'Active',
               '_openCommentPeriod': '',
               '_onlyActiveProjects': '',
               'states': '144',
               'offices': 'all',
               'projectTypes': '6',
               'fiscalYears': ['2019', '2018', '2017', '2016', '2015'],
               'projectPrograms': 'Fluid Minerals (Oil & Gas, Tar Sands, Oil Shale)',
               'projectSubprograms': 'all',
               'counties': 'all',
               'typePlanningEffort': 'all',
               'applicant': '',
               'projectName': '',
               'nepaNumber': '',
               'eisOpecNumber': '',
               'sitePageText': '',
               'intentDateOption': 'After',
               'intentDate': '',
               'decisionDateOption': 'After',
               'decisionDate': '',
               'fonsiDateOption': 'After',
               'fonsiDate': '',
               'status': status,
               'command': 'Search',
               '__ncforminfo': form_info
               }

    nepa_register_response = requests.post(
        'https://eplanning.blm.gov/epl-front-office/eplanning/nepa/nepa_register.do', headers=headers, data=payload)

    nepa_register_response_content = nepa_register_response.text
    try:
        parsed_nepa_register = BeautifulSoup(
            nepa_register_response_content, 'html.parser')
        try:
            results_table = parsed_nepa_register.find(
                "tbody", {"class": "resultsScrollContent"})
        except:
            print(status)
            print(parsed_nepa_register)
        try:
            rows = results_table.find_all("tr")
        except:
            print(status)
            # print(parsed_nepa_register)
        for row in rows:
            epl_results = row.findAll('a', {'class': 'epl_register_result'})[0]
            link = epl_results.get('href')
            result_page = requests.get(
                "https://eplanning.blm.gov/{}".format(link))
            parsed_page = BeautifulSoup(result_page.content, 'html.parser')
            data_result = parsed_page.find(
                'a', {'title': 'Display Data in current window'})[0].get('href')
            print(data_result)
    except Exception as e:
        continue
        # print(e)
