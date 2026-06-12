
import re
import phonenumbers
from pydantic import BaseModel, field_validator 

class Cliente(BaseModel): 
    nome: str 

    telefone: str
    @field_validator("telefone", mode="before")
    @classmethod
    def valida_telefone(cls, valor):

        if not valor:
            raise ValueError("Telefone é obrigatório")

        try:
            numero = phonenumbers.parse(str(valor), "BR")

            if not phonenumbers.is_valid_number(numero):
                raise ValueError("Telefone inválido")

            # Retorna apenas números no padrão brasileiro
            return str(numero.country_code) + str(numero.national_number)

        except phonenumbers.NumberParseException:
            raise ValueError("Formato de telefone inválido")
    
    email: str
    @field_validator("email", mode="before")
    @classmethod
    def valida_email(cls, valor):
        valor = valor.strip().lower()
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', valor):
            raise ValueError("Email inválido")
        return valor
    
    especialidade: str
    principal_desafio: str
