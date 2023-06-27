class Ipv4calculator:
    def __init__(self, ip):
        self.ip = ip

    def calculadoraipv4(self):
        octa = self.ip.split(".")

        if len(octa) != 4:
            raise ValueError("Endereço inválido!")
        
        nums_ip = []
        nums_bin = []

        for oct in octa:
            oct = int(oct)

            if oct < 0 or oct > 255:
                raise ValueError("Valor errado!!")

            nums_ip.append(str(oct))
            nums_bin.append(bin(int(oct))[2:].zfill(8))
        

        
        print(f'Endereço IP: {".".join(nums_ip)}')
        print(f'Endereço IP em Binário: {".".join(nums_bin)}')

ip = Ipv4calculator("10.20.12.45")

ip.calculadoraipv4()