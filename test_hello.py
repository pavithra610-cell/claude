from hello import greet, main


class TestGreet:
    def test_greet_world(self):
        assert greet("World") == "Hello, World!"

    def test_greet_custom_name(self):
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_empty_string(self):
        assert greet("") == "Hello, !"

    def test_greet_name_with_spaces(self):
        assert greet("John Doe") == "Hello, John Doe!"

    def test_greet_numeric_string(self):
        assert greet("123") == "Hello, 123!"


class TestMain:
    def test_main_output(self, capsys):
        main()
        captured = capsys.readouterr()
        assert captured.out == "Hello, World!\n"
