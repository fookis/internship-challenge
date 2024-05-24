import math
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ObterNumDiv(APIView):
    def get(self, request):
        try:
            intervaloDe = int(request.query_params.get('intervaloDe'))
            intervaloAte = int(request.query_params.get('intervaloAte'))

            if intervaloDe <= 0 or intervaloAte <= 0:
                return Response({'error': 'Por favor, informe números maiores que zero'}, status=status.HTTP_400_BAD_REQUEST)
            
            resultado = self.obterMenorNumDivisor(intervaloDe, intervaloAte)
            
            return Response({'resultado': resultado}, status=status.HTTP_200_OK)

        except (ValueError, TypeError):
            return Response({'error': 'Por favor, informe números inteiros válidos'}, status=status.HTTP_400_BAD_REQUEST)
    
    def obterMenorNumDivisor(self, x, y):
        x, y = min(x, y), max(x, y)
        
        resultado = x
        
        for num in range(x + 1, y + 1):
            resultado = abs(resultado * num) // math.gcd(resultado, num)
                
        return resultado
