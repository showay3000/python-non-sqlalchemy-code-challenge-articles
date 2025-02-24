import pytest
from classes.many_to_many import Article, Magazine, Author

class TestAuthor:
    """This class contains tests for the Author class in many_to_many.py"""

    def test_has_name(self):
        """Test if the author is correctly initialized with a name"""
        # Create two author instances with names
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        # Assert that the names of the authors are as expected
        assert author_1.name == "Carry Bradshaw"
        assert author_2.name == "Nathaniel Hawthorne"

    def test_name_is_immutable_string(self):
        """Test if the author's name is of type string and cannot be changed"""
        # Create an author instance
        author = Author("Carry Bradshaw")

        # Try to change the author's name (this should raise an error)
        with pytest.raises(AttributeError, match="Cannot modify the name attribute"):
            author.name = "ActuallyTopher"  # Trying to modify the name should raise an error

    def test_name_len(self):
        """Test if the author's name is longer than 0 characters"""
        # Create an author instance
        author = Author("Carry Bradshaw")

        # Assert that the length of the author's name is greater than 0
        assert len(author.name) > 0

    def test_has_many_articles(self):
        """Test if the author has many articles"""
        # Create an author instance and a magazine
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        
        # Add articles for the author
        article_1 = author.add_article(magazine, "How to wear a tutu with style")
        article_2 = author.add_article(magazine, "Dating life in NYC")

        # Assert that the author has two articles
        assert len(author.articles()) == 2
        assert article_1 in author.articles()  # Check if article_1 is in the list of articles
        assert article_2 in author.articles()  # Check if article_2 is in the list of articles

    def test_articles_of_type_articles(self):
        """Test if the author's articles are of type Article"""
        # Create an author instance and a magazine
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        
        # Add an article
        article = author.add_article(magazine, "How to wear a tutu with style")

        # Assert that the article is of type Article
        assert isinstance(author.articles()[0], Article)

    def test_has_many_magazines(self):
        """Test if the author has many magazines"""
        # Create an author instance
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        
        # Add articles for the author to both magazines
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_2, "2023 Eccentric Design Trends")

        # Assert that both magazines are in the author's list of magazines
        assert magazine_1 in author.magazines()
        assert magazine_2 in author.magazines()

    def test_magazines_of_type_magazine(self):
        """Test if the author's magazines are of type Magazine"""
        # Create an author instance and a magazine
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        
        # Add an article for the author
        author.add_article(magazine_1, "How to wear a tutu with style")

        # Assert that the magazine is of type Magazine
        assert isinstance(author.magazines()[0], Magazine)

    def test_magazines_are_unique(self):
        """Test if the author's magazines are unique (no duplicates)"""
        # Create an author instance and two magazines
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        
        # Add articles for the author to both magazines
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_2, "2023 Eccentric Design Trends")
        author.add_article(magazine_2, "Carrara Marble is so 2020")

        # Assert that the number of unique magazines is equal to the total number of magazines
        assert len(set(author.magazines())) == len(author.magazines())  # Check for uniqueness

    def test_topic_areas(self):
        """Test if the author can return a list of topic areas for all their articles"""
        # Create an author instance and two magazines
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        
        # Add articles for the author
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_2, "Carrara Marble is so 2020")

        # Get the list of topic areas and check if it matches the expected values
        actual_topic_areas = author.topic_areas()
        expected_topic_areas = ["Fashion", "Architecture"]
        assert sorted(actual_topic_areas) == sorted(expected_topic_areas)  # Compare the sorted lists

    def test_topic_areas_are_unique(self):
        """Test if the topic areas are unique (no duplicates)"""
        # Create an author instance and two magazines
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        
        # Add multiple articles for the author
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_1, "Dating life in NYC")
        author.add_article(magazine_2, "2023 Eccentric Design Trends")

        # Assert that the topic areas are unique (no duplicates)
        assert len(set(author.topic_areas())) == len(author.topic_areas())  # Check for uniqueness

# This allows the script to run tests when executed directly
if __name__ == "__main__":
    pytest.main([__file__])  # Run the tests when this file is executed directly
