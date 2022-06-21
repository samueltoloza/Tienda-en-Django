def importe_total_carro(request):
    total = 0
    for key, value in request.session["carro"].items():
        total = total+float(value["precio"])

    return {"importe_total_carro":total}
    # if request.user.is_authenticated:
    #     for key, value in request.session["carro"].items():
    #         total = total+(float(value["precio"])*value["cantidad"])
    # return {"importe_total_carro": total}
        # if not request.session.get("carro"):
        #     return {"importe_total_carro":total}
        # else:    
        #     for key, value in request.session["carro"].items():
        #         total = total+float(value["precio"])
        #     return {"importe_total_carro":total}
