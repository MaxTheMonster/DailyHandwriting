@app.task
def set_challenge_finished(obj):
    """
    This celery task sets the 'is_active' flag of the race object 
    to False in the database after the race end time has elapsed.
    """

    obj.has_shown = True # set the race as not active 
    obj.save() # save the race object 