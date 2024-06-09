from openai import OpenAI
cliente = OpenAI()

completo = cliente.chat.completions.create(
    model="OPENAI_API_KEY",
    messages=[
    {"role": "system", "content": "Você é um assistente poético, habilidoso em explicar conceitos complexos de programação com criatividade."},
    {"role": "user", "content": "Componha um poema que explique o conceito de recursão na programação."}],
)

print(completo.choices[0].message)