from speedtest import Speedtest
import wmi
wmodel = wmi.WMI()
none_to_print = "None"
meu_sistema = wmodel.Win32_ComputerSystem()[0]
windows_info = wmodel.Win32_OperatingSystem()[0]
disk = wmodel.Win32_LogicalDisk()
st = Speedtest()

class SistemaGeral:

    def info_geral():
            
        return print(f"Fabricante: {meu_sistema.Manufacturer}\nModelo: {meu_sistema.Model}\nNome: {meu_sistema.Name}\nSistema Operacional: {windows_info.Caption}\nVersão do Windows: {windows_info.Version}")

    def internet_speed():

        download = st.download(threads=None)*(10**-6)
        upload = st.upload(threads=None)*(10**-6)
        print(f"Download: {download:.2f} Mbps\nUpload: {upload:.2f} Mbps")

#SistemaGeral.info_geral()