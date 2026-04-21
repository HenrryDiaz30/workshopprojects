# Plataforma Serverless de Gestión de Talleres

Aplicación web serverless desarrollada en AWS para gestionar talleres de formación profesional.

El proyecto demuestra el uso de arquitecturas cloud modernas, **event-driven architecture**, **Infrastructure as Code** y **CI/CD** utilizando servicios administrados de AWS.

---

# Arquitectura del Sistema

La plataforma sigue una arquitectura **serverless y basada en eventos**.

## Flujo principal

Cliente  
↓  
CloudFront  
↓  
S3 (Frontend)

Solicitudes API  
↓  
AWS WAF  
↓  
API Gateway  
↓  
AWS Lambda  
↓  
DynamoDB

## Flujo basado en eventos

Lambda  
↓  
EventBridge  
↓  
SNS (Notificaciones por correo)

---

# Tecnologías Utilizadas

## Frontend
- Amazon S3 (hosting estático)
- Amazon CloudFront (CDN)

## Backend
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB

## Autenticación
- Amazon Cognito (JWT)

## Arquitectura basada en eventos
- Amazon EventBridge
- Amazon SNS

## Observabilidad
- Amazon CloudWatch Logs
- Amazon CloudWatch Alarms

## Seguridad
- AWS WAF
- IAM con principio de mínimo privilegio
- Autenticación con Cognito

## DevOps
- GitHub Actions (CI/CD)
- AWS SAM (Infrastructure as Code)

## Control de costos
- AWS Budgets

---

# Estructura del Proyecto
.
├ frontend
├ backend
│ └ funciones Lambda
├ infra
│ └ template.yaml
├ docs
│ ├ architecture.md
│ ├ api.md
│ ├ deployment.md
│ ├ observability.md
│ ├ security.md
│ └ costs.md
└ .github
└ workflows
└ deploy.yml

---

# Endpoints de la API

## URL base
https://<api-id>.execute-api.us-east-1.amazonaws.com/prod

---

## Obtener talleres
GET /workshops

Devuelve la lista de talleres disponibles.

---

## Crear taller
POST /workshops

Crea un nuevo taller.

---

## Registrarse a un taller
POST /workshops/{id}/register

Registra un estudiante en un taller y genera un evento en EventBridge.

---

# Despliegue

La infraestructura se despliega usando **AWS SAM**.

## Construir la infraestructura
sam build

## Desplegar infraestructura
sam deploy --guided

Esto crea automáticamente:

- API Gateway
- Funciones Lambda
- Tabla DynamoDB
- Integraciones con EventBridge

---

# CI/CD

El despliegue automático se realiza con **GitHub Actions**.

El pipeline realiza:

1. Checkout del repositorio
2. Configuración de credenciales AWS
3. Subida del frontend a S3
4. Invalidación de caché en CloudFront

Archivo del pipeline:
.github/workflows/deploy.yml

---

# Observabilidad

El sistema utiliza **Amazon CloudWatch** para monitoreo.

Incluye:

- Logs de Lambda
- Métricas de API Gateway
- Alarmas en CloudWatch
- Monitoreo de eventos

Ejemplo de alarma:
lambda-register-errors

Se activa cuando una función Lambda genera errores.

---

# Seguridad

La seguridad se implementa en varias capas.

## Autenticación
Amazon Cognito gestiona la autenticación de usuarios mediante tokens JWT.

## Protección de la API
AWS WAF protege contra ataques comunes como:

- SQL Injection
- Cross-Site Scripting (XSS)
- tráfico malicioso

## Control de acceso
IAM roles aplican el principio de **mínimo privilegio**.

---

# Control de Costos

Se configuró **AWS Budgets** para evitar gastos inesperados.

Presupuesto configurado:
workshops-budget

Tipo:
Zero Spend Budget

Se envían alertas por correo si se detecta cualquier gasto.

---

# Documentación

La documentación detallada se encuentra en la carpeta `/docs`.

Incluye:

- arquitectura
- endpoints
- despliegue
- observabilidad
- seguridad
- costos

---

# Autor

Henrry Diaz  
Estudiante de Ingeniería en Sistemas Computacionales  
Panamá

---

# Licencia

Proyecto desarrollado con fines académicos.
