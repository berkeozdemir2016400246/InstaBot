import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        time.sleep(1)

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

        popUp = self.browser.find_element_by_class_name('mt3GC')
        popUp.click()

    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()

    def unfollowWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text == 'Following'):
            followButton.click()
            time.sleep(2)
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()

    def getUserFollowers(self, username, max):
        self.browser.get('https://www.instagram.com/' + username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(2)
        #followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
        followersList = self.browser.find_element_by_class_name('isgrP')

        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
            followersList.click()
            time.sleep(0.2)

        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            followers.append(userLink)
            if (len(followers) == max):
                break
        return followers


    def likeInTag(self, tag, n):
        self.browser.get('https://www.instagram.com/explore/tags/'+tag)
        row = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]')
        img = row.find_element_by_tag_name('a')
        img.click()
        for i in range(n):
            path = '//html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button'
            #heart = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button')
            #heart.click()
            right_arrow = self.browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a[2]')
            right_arrow.click()
            time.sleep(0.5)





    def getLikesInPost(self, postUrl,f):
        self.browser.get(postUrl)
        expandButton = self.browser.find_elements_by_class_name('_8A5w5')[1]
        max = min(int(expandButton.find_element_by_tag_name('span').text.replace(',', '')),100000)
        print(str(max) + 'is max')


        expandButton.click()


        followersList = set()

        currentList = self.browser.find_elements_by_class_name('eGOV_')
        for item in currentList:
            try:
                link = item.find_element_by_tag_name('a')
            except:
                continue
            print(link.text)
        numberOfFollowersInList = len(followersList)

        actionChain = webdriver.ActionChains(self.browser)
        actionChain.key_down(Keys.TAB).key_up(Keys.TAB).key_down(Keys.TAB).key_up(Keys.TAB).perform()
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.DOWN).key_up(Keys.DOWN).perform()
            currentList = self.browser.find_elements_by_class_name('eGOV_')
            for item in currentList:
                try:
                    link = item.find_element_by_tag_name('a')
                except:
                    continue
                followersList.add(link.text)
            numberOfFollowersInList = len(followersList)
            print(numberOfFollowersInList)



        for follower in followersList:
            print(follower)
        return followersList



