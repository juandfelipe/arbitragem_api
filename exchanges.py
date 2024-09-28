import requests
import json
from decimal import Decimal, getcontext


class Picnic():
    def __init__(self):
        self.url = "https://usepicnic.com/api/swap/quote"
        self.body = {
            "fromAssetId": "eip155:137/erc20:0xc2132D05D31c914a87C6611C10748AEb04B58e8F",
            "toAssetId": "eip155:137/erc20:0xE6A537a407488807F0bbeb0038B79004f19DDDFb",
            "fromAmount": "1025000000",
            "fromWalletAddress": None,
            "toWalletAddress": None,
            "enableBRLA": False,
            "provider": None,
            "isGuest": True
        }
        self.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Cache-Control": "public, max-age=0, must-revalidate"
        }
        self.price = 0

    def get_real_quote(self, dolar_value):
        if dolar_value:
            try:
                # if network == 'bsc':
                #     self.body['fromAssetId'] = 'eip155:56/bep20:0x55d398326f99059fF775485246999027B3197955'
                # else:
                #     self.body['fromAssetId'] = 'eip155:137/erc20:0xc2132D05D31c914a87C6611C10748AEb04B58e8F'

                self.body["fromAmount"] = f"{dolar_value:.6f}".replace('.','')
                response = requests.post(self.url, headers=self.headers, data=json.dumps(self.body))

                if response.status_code == 200:
                    response.raise_for_status()  # Levanta um erro se o status da resposta não for 200
                    data = response.json()
                    
                    # Define a precisão global do Decimal para lidar com grandes números e precisão
                    getcontext().prec = 50  # Define uma precisão maior do que 18 casas decimais para garantir precisão suficiente

                    # Converte a string para Decimal
                    decimal_value = Decimal(data['toAmount'])

                    # Ajusta a escala para ter 18 casas decimais
                    adjusted_decimal_value = decimal_value / Decimal('1e18')

                    # Converte o Decimal para float
                    cotacao_brl = float(adjusted_decimal_value)

                    if cotacao_brl is None:
                        return 0
                    
                    self.price = cotacao_brl / dolar_value
                    return cotacao_brl
                else:
                    return 0
            
            except requests.RequestException as e:
                print(f"Erro ao fazer a requisição: {e}")
                return 0
            except ValueError as e:
                print(f"Erro ao processar os dados: {e}")
                return 0
            
    def get_price(self):
        return self.price
            
    def get_dolar_quote():
        pass

    def get_message():
        pass

    def get_profit():
        pass

    def get_tax():
        pass

    def set_real_quote():
        pass