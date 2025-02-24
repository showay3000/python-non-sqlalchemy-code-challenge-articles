import pytest
from classes.many_to_many import Magazine

class TestMagazine:
    """This class contains tests for the Magazine class in many_to_many.py"""

    def test_has_name(self):
        """Test if the magazine is correctly initialized with a name"""
        # Create two magazine instances
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")

        # Assert that the names are as expected
        assert magazine_1.name == "Vogue"
        assert magazine_2.name == "AD"

    def test_name_is_immutable_string(self):
        """Test if the magazine name is of type string and cannot be changed"""
        # Create two magazine instances
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")

        # Try to change the name (should raise AttributeError)
        with pytest.raises(AttributeError):
            magazine_1.name = "Vogue Italia"  # Trying to change name should raise an error

        with pytest.raises(AttributeError):
            magazine_2.name = 2  # Trying to set a non-string value should raise an error

    def test_has_category(self):
        """Test if the magazine is correctly initialized with a category"""
        # Create two magazine instances
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")

        # Assert that the categories are as expected
        assert magazine_1.category == "Fashion"
        assert magazine_2.category == "Architecture & Design"

    def test_category_is_immutable_string(self):
        """Test if the magazine category is of type string and cannot be changed"""
        # Create two magazine instances
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")

        # Try to change the category (should raise AttributeError)
        with pytest.raises(AttributeError):
            magazine_1.category = "Lifestyle"  # Trying to change category should raise an error

        with pytest.raises(AttributeError):
            magazine_2.category = 2  # Trying to set a non-string value should raise an error

    def test_get_all_magazines(self):
        """Test if all magazine instances are tracked correctly"""
        # Reset the list of magazines before the test
        Magazine.all = []
        
        # Create two magazine instances
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")

        # Assert that both magazines are added to the class-level list 'all'
        assert len(Magazine.all) == 2  # Check that the list has two magazines
        assert magazine_1 in Magazine.all  # Check if magazine_1 is in the list
        assert magazine_2 in Magazine.all  # Check if magazine_2 is in the list

# This allows the script to run tests if executed directly
if __name__ == "__main__":
    pytest.main([__file__])  # Run the tests when this file is executed directly
