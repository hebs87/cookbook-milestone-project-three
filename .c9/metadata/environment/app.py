{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":22,"position":22,"stack":[[{"start":{"row":485,"column":33},"end":{"row":486,"column":0},"action":"insert","lines":["",""],"id":1208},{"start":{"row":486,"column":0},"end":{"row":486,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":486,"column":8},"end":{"row":486,"column":12},"action":"remove","lines":["    "],"id":1209},{"start":{"row":486,"column":4},"end":{"row":486,"column":8},"action":"remove","lines":["    "]},{"start":{"row":486,"column":0},"end":{"row":486,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":486,"column":0},"end":{"row":487,"column":0},"action":"insert","lines":["",""],"id":1210}],[{"start":{"row":277,"column":0},"end":{"row":305,"column":0},"action":"remove","lines":["        insert = {","            \"name\": request.form.get(\"name\").lower(),","            \"rating_values\": [","                int(request.form.get(\"rating\"))","            ],","            \"prep_time\": request.form.get(\"prep_time\").lower(),","            \"cook_time\": request.form.get(\"cook_time\").lower(),","            \"serves\": request.form.get(\"serves\").lower(),","            \"ingredients\": request.form.getlist(\"ingredients\"),","            \"instructions\": request.form.getlist(\"instructions\"),","            \"categories\": {","                \"type\": request.form.get(\"type\").lower(),","                \"occasion\": request.form.get(\"occasion\").lower(),","                \"cuisine\": request.form.get(\"cuisine\").lower(),","                \"main_ing\": request.form.get(\"main_ing\").lower(),","            },","            \"author\": request.form.get(\"author\").lower(),","            \"img\": file_path,","            \"added_by\": user_id,","            \"added_date\": today_date,","            \"last_edited_date\": \"\",","            \"views\": 0,","            \"deleted\": False","        }","        ","        # Insert recipe dict (insert variable) into the database","        recipes_coll.insert_one(insert)","        ",""],"id":1211},{"start":{"row":277,"column":0},"end":{"row":310,"column":0},"action":"insert","lines":["        insert = {","            \"name\": request.form.get(\"name\").lower(),","            \"rating_values\": [","                int(request.form.get(\"rating\"))","            ],","            \"prep_time\": request.form.get(\"prep_time\").lower(),","            \"cook_time\": request.form.get(\"cook_time\").lower(),","            \"serves\": request.form.get(\"serves\").lower(),","            \"ingredients\": request.form.getlist(\"ingredients\"),","            \"instructions\": request.form.getlist(\"instructions\"),","            \"categories\": {","                \"type\": request.form.get(\"type\").lower(),","                \"occasion\": request.form.get(\"occasion\").lower(),","                \"cuisine\": request.form.get(\"cuisine\").lower(),","                \"main_ing\": request.form.get(\"main_ing\").lower(),","            },","            \"author\": request.form.get(\"author\").lower(),","            \"img\": file_path,","            \"added_by\": user_id,","            \"added_date\": today_date,","            \"last_edited_date\": \"\",","            \"views\": 0,","            \"likes\": 0,","            \"deleted\": False","        }","        ","        # Insert recipe dict (insert variable) into the database and get the new ID","        new_id = recipes_coll.insert_one(insert)","        ","        # Add the new recipe ID to the users collection for that user","        users_coll.update_one(","            {\"_id\": ObjectId(user_id)},","            {\"$push\": {\"added_recipes\": new_id.inserted_id}})",""]}],[{"start":{"row":310,"column":0},"end":{"row":311,"column":0},"action":"insert","lines":["",""],"id":1212}],[{"start":{"row":410,"column":35},"end":{"row":411,"column":0},"action":"insert","lines":["",""],"id":1213},{"start":{"row":411,"column":0},"end":{"row":411,"column":8},"action":"insert","lines":["        "]},{"start":{"row":411,"column":8},"end":{"row":412,"column":0},"action":"insert","lines":["",""]},{"start":{"row":412,"column":0},"end":{"row":412,"column":8},"action":"insert","lines":["        "]},{"start":{"row":412,"column":8},"end":{"row":412,"column":9},"action":"insert","lines":["#"]}],[{"start":{"row":412,"column":9},"end":{"row":412,"column":10},"action":"insert","lines":["G"],"id":1214},{"start":{"row":412,"column":10},"end":{"row":412,"column":11},"action":"insert","lines":["e"]},{"start":{"row":412,"column":11},"end":{"row":412,"column":12},"action":"insert","lines":["e"]},{"start":{"row":412,"column":12},"end":{"row":412,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":412,"column":12},"end":{"row":412,"column":13},"action":"remove","lines":["t"],"id":1215},{"start":{"row":412,"column":11},"end":{"row":412,"column":12},"action":"remove","lines":["e"]}],[{"start":{"row":412,"column":11},"end":{"row":412,"column":12},"action":"insert","lines":["t"],"id":1216}],[{"start":{"row":412,"column":12},"end":{"row":412,"column":13},"action":"insert","lines":[" "],"id":1217},{"start":{"row":412,"column":13},"end":{"row":412,"column":14},"action":"insert","lines":["n"]},{"start":{"row":412,"column":14},"end":{"row":412,"column":15},"action":"insert","lines":["u"]},{"start":{"row":412,"column":15},"end":{"row":412,"column":16},"action":"insert","lines":["m"]},{"start":{"row":412,"column":16},"end":{"row":412,"column":17},"action":"insert","lines":["b"]},{"start":{"row":412,"column":17},"end":{"row":412,"column":18},"action":"insert","lines":["e"]},{"start":{"row":412,"column":18},"end":{"row":412,"column":19},"action":"insert","lines":["r"]}],[{"start":{"row":412,"column":19},"end":{"row":412,"column":20},"action":"insert","lines":[" "],"id":1218},{"start":{"row":412,"column":20},"end":{"row":412,"column":21},"action":"insert","lines":["o"]},{"start":{"row":412,"column":21},"end":{"row":412,"column":22},"action":"insert","lines":["f"]}],[{"start":{"row":412,"column":22},"end":{"row":412,"column":23},"action":"insert","lines":[" "],"id":1219},{"start":{"row":412,"column":23},"end":{"row":412,"column":24},"action":"insert","lines":["l"]},{"start":{"row":412,"column":24},"end":{"row":412,"column":25},"action":"insert","lines":["i"]},{"start":{"row":412,"column":25},"end":{"row":412,"column":26},"action":"insert","lines":["k"]},{"start":{"row":412,"column":26},"end":{"row":412,"column":27},"action":"insert","lines":["e"]},{"start":{"row":412,"column":27},"end":{"row":412,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":412,"column":28},"end":{"row":413,"column":0},"action":"insert","lines":["",""],"id":1220},{"start":{"row":413,"column":0},"end":{"row":413,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":413,"column":8},"end":{"row":413,"column":35},"action":"insert","lines":["views = recipe.get(\"views\")"],"id":1221}],[{"start":{"row":413,"column":28},"end":{"row":413,"column":33},"action":"remove","lines":["views"],"id":1222},{"start":{"row":413,"column":28},"end":{"row":413,"column":29},"action":"insert","lines":["l"]},{"start":{"row":413,"column":29},"end":{"row":413,"column":30},"action":"insert","lines":["i"]},{"start":{"row":413,"column":30},"end":{"row":413,"column":31},"action":"insert","lines":["k"]},{"start":{"row":413,"column":31},"end":{"row":413,"column":32},"action":"insert","lines":["e"]},{"start":{"row":413,"column":32},"end":{"row":413,"column":33},"action":"insert","lines":["s"]}],[{"start":{"row":438,"column":37},"end":{"row":439,"column":0},"action":"insert","lines":["",""],"id":1223},{"start":{"row":439,"column":0},"end":{"row":439,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":439,"column":12},"end":{"row":439,"column":14},"action":"insert","lines":["\"\""],"id":1224}],[{"start":{"row":439,"column":13},"end":{"row":439,"column":14},"action":"insert","lines":["l"],"id":1225},{"start":{"row":439,"column":14},"end":{"row":439,"column":15},"action":"insert","lines":["i"]},{"start":{"row":439,"column":15},"end":{"row":439,"column":16},"action":"insert","lines":["k"]},{"start":{"row":439,"column":16},"end":{"row":439,"column":17},"action":"insert","lines":["e"]},{"start":{"row":439,"column":17},"end":{"row":439,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":439,"column":19},"end":{"row":439,"column":20},"action":"insert","lines":[":"],"id":1226}],[{"start":{"row":439,"column":20},"end":{"row":439,"column":21},"action":"insert","lines":[" "],"id":1227},{"start":{"row":439,"column":21},"end":{"row":439,"column":22},"action":"insert","lines":["l"]},{"start":{"row":439,"column":22},"end":{"row":439,"column":23},"action":"insert","lines":["i"]},{"start":{"row":439,"column":23},"end":{"row":439,"column":24},"action":"insert","lines":["k"]},{"start":{"row":439,"column":24},"end":{"row":439,"column":25},"action":"insert","lines":["e"]},{"start":{"row":439,"column":25},"end":{"row":439,"column":26},"action":"insert","lines":["s"]}],[{"start":{"row":413,"column":8},"end":{"row":413,"column":13},"action":"remove","lines":["views"],"id":1228},{"start":{"row":413,"column":8},"end":{"row":413,"column":9},"action":"insert","lines":["l"]},{"start":{"row":413,"column":9},"end":{"row":413,"column":10},"action":"insert","lines":["i"]},{"start":{"row":413,"column":10},"end":{"row":413,"column":11},"action":"insert","lines":["k"]},{"start":{"row":413,"column":11},"end":{"row":413,"column":12},"action":"insert","lines":["e"]},{"start":{"row":413,"column":12},"end":{"row":413,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":439,"column":26},"end":{"row":439,"column":27},"action":"insert","lines":[","],"id":1229}],[{"start":{"row":444,"column":4},"end":{"row":444,"column":8},"action":"remove","lines":["    "],"id":1230},{"start":{"row":444,"column":0},"end":{"row":444,"column":4},"action":"remove","lines":["    "]},{"start":{"row":443,"column":8},"end":{"row":444,"column":0},"action":"remove","lines":["",""]},{"start":{"row":443,"column":4},"end":{"row":443,"column":8},"action":"remove","lines":["    "]},{"start":{"row":443,"column":0},"end":{"row":443,"column":4},"action":"remove","lines":["    "]},{"start":{"row":442,"column":8},"end":{"row":443,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":6198,"scrollleft":0,"selection":{"start":{"row":471,"column":8},"end":{"row":471,"column":8},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":441,"state":"start","mode":"ace/mode/python"}},"timestamp":1563799788786,"hash":"fe8f2ad10d3a22c06c32346da2ea92837d613083"}