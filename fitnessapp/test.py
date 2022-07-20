# region Attachments
@app_.post('/add/attachment', summary="Ticket Add Attachments")
def ticket_add_attachments(ticket_id: int, reply_id: int, file1: UploadFile = File(None), get_company_staff: CompanyStaffs = Depends(check_token_company_staff)):
    ###################################################################
    company_staff, db = get_company_staff
    if not company_staff: return JSONResponse(status_code=401, content={'status': False, 'message': 'staff_not_found'})
    ###################################################################

    if not file1: return {'status': 'file_not_added'}

    ticket = db.execute(f"SELECT * FROM tickettickets WHERE id = '{ticket_id}' ;").fetchone()
    if not ticket: return {'status': 'ticket_not_found'}

    ticket_reply = db.execute(f"SELECT * FROM ticketreplies WHERE id = '{ticket_id}' and  content ->> 'ticket_id' = '{ticket_id}';").fetchone()
    if not ticket_reply: return {'status': 'reply_not_found'}

    ticket_attachments_path = '/static/ticket_attachments/'
    upload_folder = f'{os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(file))))}{ticket_attachments_path}'
    random_name = str(randint(1000, 999999)) + '.' + str(file1.filename).split('.')[-1]
    upload_folder_wb = open(os.path.join(upload_folder, random_name), 'wb+')
    shutil.copyfileobj(file1.file, upload_folder_wb)

    content = {"ticket_id": ticket_id, "ticket_reply_id": reply_id, "file_name": f'{ticket_attachments_path}{random_name}'}
    db_ticket_attach = mTicketAttachments(content=content)
    ac(db, db_ticket_attach)
    # path = str(os.path.join(upload_folder, random_name))
    # return {'status': 'completed', 'path': f'{ticket_attachments_path}{random_name}'}
    return {'status': 'completed'}