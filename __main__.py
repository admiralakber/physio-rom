import sanic
import airom

app = sanic.Sanic(__name__)

@app.route("/")
async def main(request):
    return sanic.response.text("Welcome... TO AI ROM")

@app.route("/process")
async def uploadvideo(request):
    # need the full stack dev
    pass

@app.route("/airom/<runid:int>/getimage")
async def getimage(request):
    pass

@app.route("/airom/<runid:int>/getangle")
async def getangle(request):
    pass

@app.route("/airom/<runid:int>/getreport")
async def getreport(request):
    return sanic.response.html(airom.postproc.postproc("","", 0))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

