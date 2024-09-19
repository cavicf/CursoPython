# CONSTANTE = "Variaveis" que não vão mudar
# muitas condições no mesmo if (ruim)
#    <- contagem de complexidade (ruim)

velocidade = 61 #velocidade atual do carro
local_carro= 90  #local em que o carro esta na estrada

RADAR_1 = 60 #velocidade máxima do radar
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #a distância onder o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
   local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('velocidade carro passou radar 1')

if carro_passou_radar_1:
    print('carro passou radar 1')

if carro_multado_radar_1:
    print('velocidade carro passou do radar 1')
