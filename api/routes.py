from flask import request, jsonify
import requests
from rabbitmq_service import enviar_mensagem
from database import db
from models import Consulta


def register_routes(app):

    @app.route("/")
    def home():
        return jsonify({
            "mensagem": "API funcionando!"
        })

    @app.route("/consultas", methods=["GET"])
    def listar_consultas():

        consultas = Consulta.query.all()

        return jsonify([
            consulta.to_dict()
            for consulta in consultas
        ])

    @app.route("/cep/<cep>", methods=["GET"])
    def consultar_cep_get(cep):

        resposta = requests.get(
            f"https://viacep.com.br/ws/{cep}/json/"
        )

        dados = resposta.json()

        consulta = Consulta(
            cep=dados.get("cep"),
            logradouro=dados.get("logradouro"),
            bairro=dados.get("bairro"),
            cidade=dados.get("localidade"),
            estado=dados.get("uf")
        )

        db.session.add(consulta)
        db.session.commit()
        enviar_mensagem({
            "cep": dados.get("cep"),
            "cidade": dados.get("localidade"),
            "estado": dados.get("uf")
            })

        return jsonify(dados)

    @app.route("/cep", methods=["POST"])
    def consultar_cep_post():

        dados_recebidos = request.get_json()

        cep = dados_recebidos["cep"]

        resposta = requests.get(
            f"https://viacep.com.br/ws/{cep}/json/"
        )

        dados = resposta.json()

        consulta = Consulta(
            cep=dados.get("cep"),
            logradouro=dados.get("logradouro"),
            bairro=dados.get("bairro"),
            cidade=dados.get("localidade"),
            estado=dados.get("uf")
        )

        db.session.add(consulta)
        db.session.commit()
        enviar_mensagem({
            "cep": dados.get("cep"),
            "cidade": dados.get("localidade"),
            "estado": dados.get("uf")
            })

        return jsonify(dados)