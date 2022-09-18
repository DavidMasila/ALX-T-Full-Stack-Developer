from flask import jsonify, redirect, request, url_for, abort, render_template
from app import app, Plant, db, migrate

#implementing CORS
@app.after_request
def after_request(response):
    response.headers.add(
        "Access-Control-Allow-Headers","Content-Type, Authorization"
    )
    response.headers.add(
        "Acess-Control-Allow-Methods","GET, POST, PATCH, DELETE, OPTIONS"
    )
    return response

@app.route('/plants', methods=['GET','POST'])
def get_plants():
    #implement pegination
    page=request.args.get('page',1,type=int) #GET PAGE otherwise default to 1
    start = (page -1)
    end = start + 10
    plants = Plant.query.all()
    formatted_plants = [plant.format() for plant in plants]

    return jsonify({
        "success":True,
        "plants": formatted_plants[start:end],
        "Total plants": len(formatted_plants)
    })

@app.route('/plants/<int:plant_id>')
def get_specified_plant(plant_id):
    plant=Plant.query.filter(Plant.id==plant_id).one_or_none()

    if plant is None:
        abort (404)
    else:
        return jsonify({
            "success":True,
            "plant":plant.format()
        })


