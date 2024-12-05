from src.phonebook import Phonebook

class TestPhonebook:

    def test_add_entrada_nao_existente(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Numero adicionado")
        resultado = phonebook.add("matheus", "800")

        assert resultado == resultadoEsperado


    def test_add_entrada_existente(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.add("POLICIA", "190")

        assert resultado == resultadoEsperado


    def test_add_entrada_nome_nulo(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.add(None, "800")

        assert resultado == resultadoEsperado


    def test_add_entrada_nome_diferente_de_string(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.add(123, "800")

        assert resultado == resultadoEsperado


    def test_add_entrada_numero_none(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Numero invalido")
        resultado = phonebook.add("matheus", None)

        assert resultado == resultadoEsperado


    def test_add_entrada_numero_diferente_de_string(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Numero invalido")
        resultado = phonebook.add("matheus", 800)

        assert resultado == resultadoEsperado


    def test_add_caractere_invalido_hashtag(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.add("matheus#", "801")

        assert resultado == resultadoEsperado


    def test_add_caractere_invalido_arroba(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.add("matheus@", "801")

        assert resultado == resultadoEsperado


    def test_add_caractere_invalido_exclamacao(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.add("matheus!", "801")

        assert resultado == resultadoEsperado


    def test_add_caractere_invalido_cifrao(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.add("matheus$", "801")

        assert resultado == resultadoEsperado


    def test_add_caractere_invalido_percentual(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.add("matheus%", "801")

        assert resultado == resultadoEsperado


    def test_lookup(self):

        phonebook = Phonebook()
        entrada = ("POLICIA","190")
        resultado = phonebook.lookup("POLICIA")

        assert resultado == entrada


    def test_lookup_nome_nulo(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.lookup(None)

        assert resultado == resultadoEsperado


    def test_lookup_nome_diferente_de_string(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.lookup(123)

        assert resultado == resultadoEsperado


    def test_lookup_caractere_invalido_hashtag(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.lookup("matheus#")

        assert resultado == resultadoEsperado


    def test_lookup_caractere_invalido_arroba(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.lookup("matheus@")
        assert resultado == resultadoEsperado


    def test_lookup_caractere_invalido_exclamacao(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.lookup("matheus!")
        assert resultado == resultadoEsperado


    def test_lookup_caractere_invalido_cifrao(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.lookup("matheus$")
        assert resultado == resultadoEsperado


    def test_lookup_caractere_invalido_percentual(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.lookup("matheus%")
        assert resultado == resultadoEsperado


    def test_get_names (self):

        phonebook = Phonebook()
        resultadoEsperado = ['POLICIA', 'matheus', 'duda']
        phonebook.add("matheus", "1")
        phonebook.add("duda", "2")

        assert phonebook.get_names() == resultadoEsperado


    def test_get_numbers (self):

        phonebook = Phonebook()
        resultadoEsperado =  ["190", "1", "2"]
        phonebook.add("matheus", "1")
        phonebook.add("duda", "2")

        assert  list(phonebook.get_numbers()) == resultadoEsperado


    def test_clear (self):

        phonebook = Phonebook()

        assert phonebook.clear()


    def test_search (self):

        phonebook = Phonebook()
        pesquisaEsperada = [{"2", 'matheus'}]
        phonebook.add("matheus", "2")
        phonebook.add("mat", "7")
        phonebook.add("duda", "19")
        phonebook.search("matheus")

        assert phonebook.search("matheus") == pesquisaEsperada


    def test_search_search_name_nulo(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.search(None)

        assert resultado == resultadoEsperado


    def test_search_search_name_diferente_de_string(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.search(123)

        assert resultado == resultadoEsperado


    def test_get_phonebook_sorted (self):

        phonebook = Phonebook()
        lista_ordenada = [('POLICIA', "190"), ("abc", "19"), ("duda", "7"), ("matheus", "2")]
        phonebook.add("matheus", '2')
        phonebook.add("duda", '7')
        phonebook.add("abc", "19")

        assert phonebook.get_phonebook_sorted() == lista_ordenada


    def test_get_phonebook_reverse (self):

        phonebook = Phonebook()
        lista_reversa = [('matheus', "3"), ('duda', "2"), ("POLICIA", "190")]
        phonebook.add("duda", "2")
        phonebook.add("matheus", "3")

        assert  phonebook.get_phonebook_reverse() == lista_reversa


    def test_delete (self):

        phonebook = Phonebook()
        phonebook.add("matheus", "1")
        phonebook.add("duda", "2")
        phonebook.delete("matheus")
        for name in phonebook.get_names():

            assert name != "matheus", "Deleção realizada"


    def test_delete_nome_nulo(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.delete(None)

        assert resultado == resultadoEsperado


    def test_delete_nome_diferente_de_string(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        resultado = phonebook.delete(123)

        assert resultado == resultadoEsperado


    def test_change_number (self):

        phonebook = Phonebook()
        resultadoEsperado = ("matheus","1000")
        phonebook.add("matheus", "1")
        phonebook.add("duda", "2")
        resultado = phonebook.change_number("matheus","1000")

        assert resultado == resultadoEsperado


    def test_change_number_nome_nulo(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Numero invalido")
        phonebook.add("matheus", "1")
        phonebook.add("duda", "2")
        resultado = phonebook.change_number("matheus", None)

        assert resultado == resultadoEsperado


    def test_change_number_nome_diferente_de_string(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Nome invalido")
        phonebook.add("matheus", "1")
        phonebook.add("duda", "2")
        resultado = phonebook.change_number(123, 123)

        assert resultado == resultadoEsperado


    def test_change_number_numero_nulo(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Numero invalido")
        resultado = phonebook.change_number("Abc",None)

        assert resultado == resultadoEsperado


    def test_change_number_numero_diferente_de_string(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Numero invalido")
        phonebook.add("matheus", "1")
        resultado = phonebook.change_number("matheus",123)

        assert resultado == resultadoEsperado


    def test_get_name_by_number(self):

        phonebook = Phonebook()
        resultadoEsperado = ("matheus")
        phonebook.add("matheus", "1000")
        resultado = phonebook.get_name_by_number("1000")

        assert resultado == resultadoEsperado


    def test_get_name_by_number_numero_nulo(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Numero invalido")
        resultado = phonebook.get_name_by_number(None)

        assert resultado == resultadoEsperado


    def test_get_name_by_number_numero_diferente_de_string(self):

        phonebook = Phonebook()
        resultadoEsperado = ("Numero invalido")
        resultado = phonebook.get_name_by_number(800)

        assert resultado == resultadoEsperado

