class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """

        if not isinstance(name, str) or name == None:
            return 'Nome invalido'
            # Adicionada validação para verificar se nome é string

        if not isinstance(number, str):
            return 'Numero invalido'
        # Adicionada validação para verificar se número é string

        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nome invalido'
        # Retorno com texto incorreto
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido'
        # Retorno com texto incorreto
        if '%' in name:
            return 'Nome invalido'

        if len(number) == 0:
        # Retirar o len ou substituir por len(str(number))
            return 'Numero invalido'
        # Retorno com texto incorreto

        if name not in self.entries:
            self.entries[name] = number
            # Não há retorno
            return 'Numero adicionado'
            # Função redundante

        return 'Nome invalido'


    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if not isinstance(name, str):
            return 'Nome invalido'
        # Adicionada validação para verificar se nome é string

        if '#' in name:
            return 'Nome invalido'
        # Retorno com texto incorreto
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nome invalido'
        # Retorno com texto incorreto
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido'
        # Retorno com texto incorreto

        if len(name) == 0:
            return 'Nome invalido'


        return name, self.entries[name]
        # Erro no retorno, erro só traz o número, em vez do número com o nome
        # Insira o "name," antes do self


    def get_names(self):
        """
        :return: return all names in phonebook
        """

        return list(self.entries.keys())


    def get_numbers(self):
        """
        :return: return all numbers in phonebook
        """

        return self.entries.values()


    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """

        self.entries = {}
        return 'phonebook limpado'


    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """

        if isinstance(search_name, str) and len(search_name) == 0:
            return 'Nome invalido'

        if not isinstance(search_name, str):
            return 'Nome invalido'


        result = []
        for name, number in self.entries.items():
            if search_name  in name:
                result.append({name, number})
        return result
    # Está incluindo apenas os nomes que não estão na pesquisa
    # Deve retornar/ adicionar os nomes que estão na pesquisa
    # Retire o "not" do if

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        # Não há implementação da função sorted()
        return sorted(self.entries.items())

    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order
        """
        # Não há implementação de função para reverter as entradas
        return sorted(self.entries.items(), reverse=True)

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """

        if isinstance(name, str) and len(name) == 0:
            return 'Nome invalido'

        if not isinstance(name, str):
            return 'Nome invalido'


        self.entries.pop(name)
        return 'Numero deletado'


    def change_number (self,name, number):

        if isinstance(name, str) and len(name) == 0:
            return 'Nome invalido'

        if  isinstance(number, str) and len(number) == 0:
            return 'Numero invalido'

        if not isinstance(name, str):
            return 'Nome invalido'

        if not isinstance(number, str):
            return 'Numero invalido'


        if name in self.entries:
            self.entries[name] = number
            return name, self.entries[name]


    def get_name_by_number(self,number):

        if not isinstance(number, str):
            return 'Numero invalido'

        if len(number) == 0:
            return 'Numero invalido'

        for nome, numero in self.entries.items():
            if number == numero:
                return nome


