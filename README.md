# 🐍 Python API com Flask + DevSecOps Pipeline

Uma pequena API desenvolvida com **FastAPI**, containerizada com **Docker** e integrada a um pipeline CI/CD no **GitHub Actions** com verificação de segurança via **OWASP ZAP**.

---

## 🚀 Endpoints

- `GET /status`  
  Retorna o status da API.

---

## 🛠️ Como rodar localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. Instale as dependências (opcional, se quiser rodar fora do Docker):
```bash
pip install -r requirements.txt
```

3. Rode com Docker:
```bash
docker build -t python-app .
docker run -p 8000:8000 python-app
```
Ou usando docker-compose com o ZAP:
```bash
docker-compose -f docker-compose.zap.yml up
```

## 🔁 Etapas do Pipeline

### 🔍 Security Scan

- 🐳 Faz build da imagem Docker e inicia a API
- ⏱️ Aguarda o container estar disponível (resposta HTTP OK)
- 🛡️ Executa um scan de segurança automatizado com **OWASP ZAP**
- 📄 Gera e salva os seguintes relatórios:
  - `report_html.html`
  - `report_md.md`
  - `report_json.json`

---

### 🚀 Deploy

- 🐳 Faz o build da imagem com Docker
- 🔐 Realiza login no Docker Hub com credenciais seguras
- 📤 Envia (push) da imagem para o Docker Hub
- 📦 Faz o deploy via **SSH** em servidor remoto (ex: EC2), utilizando Docker

---

## 🛡️ Ferramentas de Segurança Utilizadas

- **OWASP ZAP**: verificação de segurança automatizada via Docker
- **GitHub Secrets**: uso de variáveis sensíveis de forma segura
- **Proteção de Branch**: recomenda-se permitir deploy apenas nas branches `main` ou `release`


## 📄 Relatório de Segurança

O relatório gerado pelo ZAP pode ser acessado após cada execução do pipeline:

- 🔗 [Relatório HTML (ZAP)](./zap-report/report_html.html)
- 📄 [Relatório Markdown (ZAP)](./zap-report/report_md.md)

⚠️ **Atenção**: os relatórios são armazenados como *artefatos* da execução do pipeline e **não são versionados diretamente** no repositório.

---

## 🧠 Registro de Decisões Técnicas

| Decisão            | Justificativa                                                        |
|--------------------|----------------------------------------------------------------------|
| Uso de Docker      | Facilita build e deploy em diferentes ambientes                      |
| FastAPI            | Simples e rápido para pequenas APIs                                  |
| GitHub Actions     | Pipeline gratuito e nativo do GitHub                                 |
| ZAP via Docker     | Scan de segurança automatizado e sem dependências extras             |

## 🔁 Rollback - Como reverter um deploy com falha
Caso o deploy cause problemas, siga um destes métodos:

### 🔙 1. Reverter para um commit anterior
```bash
git checkout <hash-estável>
git push origin HEAD:main
```
Ou crie uma branch de rollback:
```bash
git checkout -b rollback-fix <hash-estável>
git push origin rollback-fix
```
⚠️ Se houver proteção de branch, será necessário criar um Pull Request com a reversão.


### 📦 2. Reverter imagem no servidor
Se desejar reverter diretamente no servidor:
```bash
# Substitua "old-tag" pela tag da versão estável
sudo docker pull seuusuario/python-app:old-tag
sudo docker stop python-app
sudo docker rm python-app
sudo docker run -d --name python-app -p 80:8000 seuusuario/python-app:old-tag
```

# 📋 Requisitos para Deploy

# - Docker deve estar instalado no servidor remoto
# - SSH configurado com chave privada (armazenada como SSH_PRIVATE_KEY no GitHub Secrets)

# 🔐 Secrets obrigatórios no GitHub Actions:
# - DOCKER_USERNAME
# - DOCKER_PASSWORD
# - SSH_PRIVATE_KEY
# - SSH_USER
# - SSH_HOST

# 💡 Melhorias Futuras (para evolução do projeto):
# - Implementar testes automatizados
# - Adicionar monitoramento com Prometheus e Grafana
# - Incluir linting e formatação automática
# - Utilizar estratégia de deploy blue/green ou canário

# ✅ Feito com ❤️ por [Greg]
