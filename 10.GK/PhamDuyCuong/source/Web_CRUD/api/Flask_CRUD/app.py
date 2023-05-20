#!/usr/bin/env python
import logging
import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId
from Flask_CRUD.db import init_db


title = "VDT 2023"
heading = "Danh sách học viên VDT 2023"


def redirect_url():
    return request.args.get("next") or request.referrer or url_for("index")


def create_app(students):
    app = Flask(
        __name__, template_folder="../templates/", static_folder="../static/styles"
    )

    @app.route("/")
    def todo():
        return render_template("index.html", data=list(students.find({})))

    @app.route("/action_add", methods=["POST"])
    def action_add():
        # Adding a attendee
        attendee = request.form.to_dict()
        students.insert_one(dict(attendee))

        return redirect("/")

    @app.route("/remove", methods=["DELETE"])
    def remove():
        key = request.values.get("_id")
        students.delete_one({"_id": ObjectId(key)})

        return redirect("/")

    @app.route("/update")
    def update():
        id = request.values.get("_id")
        edit_student = students.find_one({"_id": ObjectId(id)})
        return render_template(
            "update.html", edit_student=edit_student, h=heading, t=title
        )

    @app.route("/action_update", methods=["POST"])
    def action_update():
        # Updating a Task with various references
        attendee = request.form.to_dict()
        id = request.args.get("_id")
        students.update_one({"_id": ObjectId(id)}, {"$set": attendee})
        logger = logging.getLogger()
        logger.warning("Cann't connect to database")
        return redirect("/")

    @app.route("/search", methods=["GET"])
    def search():
        # Searching a Task with various references
        key = request.values.get("key")
        refer = request.values.get("refer")
        search_list = students.find({refer: {"$regex": key}})
        return render_template("searchlist.html", data=search_list, title=title)

    return app
