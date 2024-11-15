from pathlib import Path

path_file = Path(__file__).parent / 'log.txt'

class Log:
    def _logar(self, msg):
        raise NotImplementedError('Método não implementado')
    
    def logar_erro(self, msg):
        return self._logar(f"ERRO: {msg}")
    
    def logar_sucesso(self, msg):
        return self._logar(f"SUCESSO: {msg}")
    
    
class LogPrintMixin(Log):
    def _logar(self, msg):
        print(f"Log: {msg} (classe: {self.__class__.__name__})")

class LogFileMixin(Log):
    def _logar(self, msg):
        print("Salvando log no arquivo...")
        with open(path_file, 'a') as f:
            f.write(f"Log: {msg} (classe: {self.__class__.__name__})\n")

if __name__ == "__main__":
    log = LogPrintMixin()
    log._logar("Mensagem de log")
    log.logar_erro("Mensagem de erro")
    log.logar_sucesso("Mensagem de sucesso")

    log_file = LogFileMixin()
    log_file._logar("Mensagem de log")
    log_file.logar_erro("Mensagem de erro")
    log_file.logar_sucesso("Mensagem de sucesso")