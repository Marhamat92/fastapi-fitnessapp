from fastapi import APIRouter

from base_engine import SessionLocal
from models import FitnessApp, mMemberTemplate

router = APIRouter()

@router.post("/member/create",description="it creates member details for fitness app" ,summary="it creates member details")
def create_member(memberinfo:FitnessApp):
    db=SessionLocal()
    create_member=mMemberTemplate(
        member_name=memberinfo.member_name,
        member_surname=memberinfo.member_surname,
        member_email=memberinfo.member_email,
        member_city=memberinfo.member_city,
        member_age=memberinfo.member_age
    )

    db.add(create_member)
    db.commit()

    db.close()
    return "Member Details was created"

@router.get("/member/get", description="it gets each member details" ,summary="it gets member details")
def get_member(member_id:int):
    db=SessionLocal()
    get_member=db.query(mMemberTemplate).filter(mMemberTemplate.id==member_id).first()
    if not get_member:
        db.close()
        return "member details not found"

    db.close()
    return get_member

@router.get("/member/get/list",description="You can see all members as below",summary="it lists all members")
def get_member_list():
    db=SessionLocal()
    get_member_list=db.query(mMemberTemplate).all()
    if not get_member_list :
        db.close()
        return "Member list is empty"

    db.close()
    return get_member_list

@router.put("/member/update",description="you can update each member as below", summary="update each member")
def update_member(member_id:int,memberinfo:FitnessApp):
    db=SessionLocal()
    get_member=db.query(mMemberTemplate).filter(mMemberTemplate.id==member_id).first()
    if not get_member :
        db.close()
        return "record not found"

    get_member.member_name=memberinfo.member_name
    get_member.member_surname=memberinfo.member_surname
    get_member.member_email=memberinfo.member_email
    get_member.member_age=memberinfo.member_age
    get_member.member_city=memberinfo.member_city
    db.commit()

    db.close()
    return "Member info updated"

@router.delete("/member/delete",description="you can delete each member with one request as below",summary="it deletes each member")
def delete_memeber(member_id:int):
    db=SessionLocal()
    get_member=db.query(mMemberTemplate).filter(mMemberTemplate.id==member_id).first()
    if not get_member :
        db.close()
        return "record not found"
    db.delete(get_member)
    db.commit()

    db.close()
    return "Member was deleted"