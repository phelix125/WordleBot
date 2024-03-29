from logging import exception
import requests
import random
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import re
import random
from selenium.webdriver.common.action_chains import ActionChains
from WordlyPy import WordlyPy



def sendWord(guess,actions):
    actions.send_keys(guess)
    actions.perform()
    sleep(1)
    actions.send_keys(u'\ue007')
    actions.perform()
    sleep(2)
    actions.send_keys(Keys.RETURN)
    actions.perform()

def checkWords(driver,wp,row):
    win = 0
    for i in range(1,6):
        letterElement = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/div[2]/div['+str(row)+']/div['+ str(i) +']')
        
        letter = letterElement.text[0]
        letter = letter.lower()
        if(letterElement.get_attribute('innerHTML').find("absent") != -1):
            wp.filterBannedChar(letter)
        elif(letterElement.get_attribute('innerHTML').find("present")!= -1):
            wp.filterContainChar(letter,i-1)
        elif(letterElement.get_attribute('innerHTML').find("correct") != -1):
            win += 1
            wp.filterIndexChar(letter,i-1)
        
    return win == 5
            


def main():
    with open("words.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    wp = WordlyPy(lines, 2)
    wp.cleanText()
    
    site = "https://wordplay.com/new"
    driver = webdriver.Safari()
    driver.get(site)
    actions = ActionChains(driver)
    sleep(3)
    actions.move_by_offset(20,20).click().perform()
    #//*[@id="mainstart"]/div[2]/button[1]
    sleep(3)
    wp.printFilters()

    for i in range(1,7):
        word = wp.popRandWord()
        # OPTIONAL wp.popSmartWord() -> NOTE: doesn't work quite as well.
        print(word)
        sendWord(word,actions)
    
        sleep(5)
        if(checkWords(driver,wp,i)):
            print("DONE: Word was ",word)
            break
        #wp.printGuessWords()
        actions.send_keys(Keys.ENTER)
        actions.perform()
        wp.printFilters()

    
    

    
        

if __name__ == "__main__":

    main()