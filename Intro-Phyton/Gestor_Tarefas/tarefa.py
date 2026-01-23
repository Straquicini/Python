class Tarefa:
    def __init__(self, titulo, descricao, dataLimit, concluida):   
        self._titulo = titulo
        self._descricao = descricao
        self._data_limite = dataLimit
        self._concluida = concluida = False


    # Getters
    @property
    def get_titulo(self):
        return self._titulo

    @property
    def get_descricao(self):
        return self._descricao

    @property
    def get_data_limite(self):
        return self._data_limite

    @property
    def get_concluida(self):
        return self._concluida
    
    # Setters importantes
    def set_concluida(self, concluida):
        self._concluida = concluida
