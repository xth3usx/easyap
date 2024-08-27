from config import URL_ADMIN_ROUTER, SENHA_ADMIN_ROUTER, SENHA_GESTAO_SSID, \
                    NOME_SSID_2G, NOME_SSID_5G, MASCARA_SUBREDE, GATEWAY_PADRAO, \
                    DNS_PRIMARIO, DNS_SECUNDARIO, NOME_GRUPO_ISOLAMENTO


def processar_mascara_subrede(MASCARA_SUBREDE):
    # Dividir a máscara de sub-rede em octetos
    octetos = MASCARA_SUBREDE.split('.')

    # Verificar se a entrada possui exatamente 4 octetos
    if len(octetos) == 4:
        try:
            # Converter cada octeto para inteiro
            mask1, mask2, mask3, mask4 = [int(octeto) for octeto in octetos]
            
            # Verificar se cada octeto está no intervalo válido (0 a 255)
            if all(0 <= octeto <= 255 for octeto in [mask1, mask2, mask3, mask4]):
                return mask1, mask2, mask3, mask4
            else:
                raise ValueError("Cada octeto deve estar no intervalo de 0 a 255.")
        except ValueError as e:
            raise ValueError(f"Entrada inválida: {e}")
    else:
        raise ValueError("Máscara de sub-rede inválida. Certifique-se de que está no formato xxx.xxx.xxx.xxx.")

def processar_gateway_padrao(GATEWAY_PADRAO):
    # Dividir o endereço IP do gateway padrão em octetos
    octetos = GATEWAY_PADRAO.split('.')

    # Verificar se a entrada possui exatamente 4 octetos
    if len(octetos) == 4:
        try:
            # Converter cada octeto para inteiro
            gtw1, gtw2, gtw3, gtw4 = [int(octeto) for octeto in octetos]
            
            # Verificar se cada octeto está no intervalo válido (0 a 255)
            if all(0 <= octeto <= 255 for octeto in [gtw1, gtw2, gtw3, gtw4]):
                return gtw1, gtw2, gtw3, gtw4
            else:
                raise ValueError("Cada octeto deve estar no intervalo de 0 a 255.")
        except ValueError as e:
            raise ValueError(f"Entrada inválida: {e}")
    else:
        raise ValueError("Endereço IP inválido. Certifique-se de que está no formato xxx.xxx.xxx.xxx.")

def processar_dns_primario(DNS_PRIMARIO):
    # Dividir o endereço IP do DNS primário em octetos
    octetos = DNS_PRIMARIO.split('.')

    # Verificar se a entrada possui exatamente 4 octetos
    if len(octetos) == 4:
        try:
            # Converter cada octeto para inteiro
            dns1_1, dns1_2, dns1_3, dns1_4 = [int(octeto) for octeto in octetos]
            
            # Verificar se cada octeto está no intervalo válido (0 a 255)
            if all(0 <= octeto <= 255 for octeto in [dns1_1, dns1_2, dns1_3, dns1_4]):
                return dns1_1, dns1_2, dns1_3, dns1_4
            else:
                raise ValueError("Cada octeto deve estar no intervalo de 0 a 255.")
        except ValueError as e:
            raise ValueError(f"Entrada inválida: {e}")
    else:
        raise ValueError("Endereço IP inválido. Certifique-se de que está no formato xxx.xxx.xxx.xxx.")
    
def processar_dns_secundario(DNS_SECUNDARIO):
    # Dividir o endereço IP do DNS secundário em octetos
    octetos = DNS_SECUNDARIO.split('.')

    # Verificar se a entrada possui exatamente 4 octetos
    if len(octetos) == 4:
        try:
            # Converter cada octeto para inteiro
            dns2_1, dns2_2, dns2_3, dns2_4 = [int(octeto) for octeto in octetos]
            
            # Verificar se cada octeto está no intervalo válido (0 a 255)
            if all(0 <= octeto <= 255 for octeto in [dns2_1, dns2_2, dns2_3, dns2_4]):
                return dns2_1, dns2_2, dns2_3, dns2_4
            else:
                raise ValueError("Cada octeto deve estar no intervalo de 0 a 255.")
        except ValueError as e:
            raise ValueError(f"Entrada inválida: {e}")
    else:
        raise ValueError("Endereço IP inválido. Certifique-se de que está no formato xxx.xxx.xxx.xxx.")