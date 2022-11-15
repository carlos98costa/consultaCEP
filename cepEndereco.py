from gerador_endereco import *
import PySimpleGUI as sg

def tela_inicial():
    sg.theme('Dark')
    layout_inicial = [[sg.T('Informe o CEP:'), sg.Input(k='-CEP-', background_color='gray')],
                      [sg.T('Logradouro:'), sg.Input(k='-RUA-', disabled=True, disabled_readonly_background_color='gray')],
                      [sg.T('Bairro:'), sg.Input(k='-BAIRRO-', disabled=True, disabled_readonly_background_color='gray')],
                      [sg.T('Complemento:'), sg.Input(k='-COMPLEMENTO-', disabled=True, disabled_readonly_background_color='gray')],
                      [sg.T('Cidade:'), sg.Input(k='-CIDADE-', disabled=True, disabled_readonly_background_color='gray')],
                      [sg.T('UF:'), sg.Input(k='-UF-', disabled=True, disabled_readonly_background_color='gray')],
                      [sg.Button('Buscar')]
                     ]

    return sg.Window('Buscar CEP', layout=layout_inicial, finalize=True)

janela1 = tela_inicial()

while True:
    window, event, values = sg.read_all_windows()

    # Fechando a interface
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if window == janela1 and event == 'Buscar':
        cepBuscar = values['-CEP-']
        #address0 = get_address_from_cep(cepBuscar, webservice=WebService.CORREIOS)
        #address1 = get_address_from_cep(cepBuscar, webservice=WebService.VIACEP)
        address2 = get_address_from_cep(cepBuscar, webservice=WebService.APICEP)
        rua = address2['logradouro']
        bairro = address2['bairro']
        cidade = address2['cidade']
        uf = address2['uf']
        complemento = address2['complemento']
        window['-RUA-'].update(rua)
        window['-BAIRRO-'].update(bairro)
        window['-CIDADE-'].update(cidade)
        window['-UF-'].update(uf)
        window['-COMPLEMENTO-'].update(complemento)



