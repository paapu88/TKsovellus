# -*- coding: utf-8 -*-

#opettajaan liittyvät tietokantahaut

#@auth.requires_membership('opettaja')
def hae_opettajan_kaikki_kurssit():
    #haetaan tietokannasta kaikki opettajan kurssit
    query = (db.opettaja.id == db.auth_user.id)&\
        (db.kurssi.opettaja_id == db.opettaja.id)
    return db(query).select()

def hae_kurssin_kurssityot(kurssi_id):
    #haetaan tietokannasta kaikki kurssin kurssityöt
    query = (kurssi_id == db.kurssityo.kurssi_id)
    return SQLFORM.grid(query)
    #return db(query).select()
