class Article:
    # List to store all articles created
    all = []

    def __init__(self, author, magazine, title):
        # Initialize the article with author, magazine, and title
        if not (5 <= len(title) <= 50):  # Ensure the title length is between 5 and 50 characters
            raise ValueError("Title length must be between 5 and 50 characters inclusive")
        self.author = author  # Assign the author to the article
        self.magazine = magazine  # Assign the magazine to the article
        self._title = title  # Store the title (it's private to protect it)
        Article.all.append(self)  # Add the article to the global list of articles

    @property
    def title(self):
        # Return the title of the article
        return self._title

    @title.setter
    def title(self, value):
        # Prevent modification of the title after it's set
        raise AttributeError("Title attribute is immutable")

    @title.deleter
    def title(self):
        # Prevent deletion of the title
        raise AttributeError("Title attribute cannot be deleted")


class Author:
    def __init__(self, name):
        self._name = name  # Store the author's name (it's private to protect it)
        self._articles = []  # Initialize an empty list to hold the author's articles

    @property
    def name(self):
        # Return the name of the author
        return self._name

    @name.setter
    def name(self, value):
        # Prevent modification of the author's name after it's set
        raise AttributeError("Cannot modify the name attribute")

    def add_article(self, magazine, title):
        # Add an article written by the author to a magazine
        article = Article(self, magazine, title)  # Create a new article
        self._articles.append(article)  # Add the article to the author's article list
        return article  # Return the created article

    def articles(self):
        # Return the list of articles written by the author
        return self._articles

    def magazines(self):
        # Return a list of unique magazines the author has written for
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        # Return a list of unique categories (topic areas) for magazines the author has written for
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    # List to store all magazines created
    all = []

    def __init__(self, name, category):
        self._name = name  # Store the name of the magazine (it's private to protect it)
        self._category = category  # Store the category of the magazine (it's private to protect it)
        self._articles = []  # Initialize an empty list to hold the magazine's articles
        self._contributors = []  # Initialize an empty list to hold the magazine's contributors
        Magazine.all.append(self)  # Add the magazine to the global list of magazines

    @property
    def name(self):
        # Return the name of the magazine
        return self._name

    @name.setter
    def name(self, value):
        # Prevent modification of the magazine's name after it's set
        raise AttributeError("Cannot modify the name attribute")

    @property
    def category(self):
        # Return the category of the magazine
        return self._category

    @category.setter
    def category(self, value):
        # Prevent modification of the magazine's category after it's set
        raise AttributeError("Cannot modify the category attribute")

    def add_article(self, article):
        # Add an article to the magazine's list of articles
        self._articles.append(article)

    def articles(self):
        # Return the list of articles published in the magazine
        return self._articles

    def add_contributor(self, author):
        # Add an author as a contributor to the magazine
        self._contributors.append(author)

    def contributors(self):
        # Return a list of authors who have contributed to the magazine
        return self._contributors

    def article_titles(self):
        # Return a list of titles of all articles in the magazine
        return [article.title for article in self._articles]

    def contributing_authors(self):
        # Return a list of authors who have contributed to the magazine
        return [article.author for article in self._articles]
