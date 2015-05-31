from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AddNewMovieTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_add_new_movie_into_database(self):
        # Vivek decides to visit our wonderful website to see
        # the reviews on the movie he just watched.
        self.browser.get(self.live_server_url)

        # He sees that he's reached the right page, the Media Database.
        self.assertIn('Media Database', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Media Database', header_text)

        # He tries to search for his movie by typing the movie title
        # into the search bar. He searches for Pam Anderson in Vegas
        inputbox = self.browser.find_element_by_id('search_query')
        inputbox.send_keys('Pam Anderson in Vegas')
        inputbox.send_keys(Keys.ENTER)

        # The loaded page shows no results. This amazing movie hasn't been added!
        self.fail()

        # Vivek is determined to add the movie. He clicks the Add Movie button.

        # He fills out the title, rating, summary, and genre, but leaves the optional
        # fields like review, year, or actors empty.

        # He submits and sees his new page.

        # He searches for Pam Anderson in Vegas to make sure the newly
        # added media shows up.

        # He's happy. But he realizes that the long summary he wrote was for the
        # sequel, Pam Anderson Meets Tila Tequila. He decides to delete the page
        # and add a new one.

        # He searches again to make sure it still works. It does.

        # Vivek loves the movie so much he decides to fill out the rest of the
        # fields. He hits the edit page button and does so.