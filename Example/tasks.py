from robocorp.tasks import task
from RPA.Desktop.Windows import Windows
from RPA.Desktop import Desktop
import time

windows = Windows()
desktop = Desktop()

@task
def minimal_task():
    windows.open_from_search('chrome.exe','New Tab - Google Chrome')
    
    windows.send_keys_to_input('https://taxpayerportal.ird.gov.np/taxpayer/app.html', True)
    desktop.click('image:general.png','double_click' ) 
    desktop.click('image:Taxplayer.png','double_click' )

    desktop.click('image:pannumber.png' )
    desktop.type_text('132981446')
    desktop.press_keys('tab')

    desktop.type_text('132981446')
    desktop.press_keys('tab')
    
    desktop.type_text('nepal@123')
    desktop.click('image:login.png' )
    time.sleep(3)

    desktop.click('image:withhold.png' )
    desktop.click('image:bsad.png' )
    desktop.type_text('BS')
    # desktop.click('image:bs.png' )
    desktop.press_keys('tab')

    desktop.type_text('2060.05.05')
    desktop.press_keys('tab')

    desktop.type_text('2077.12.03')
    desktop.click('image:search.png' )
    desktop.click('image:save.png' )
