import requests
import json

from decouple import config

import logging
logging.basicConfig()
# Get an instance of a logger
logger = logging.getLogger(__name__)

def send_notes(request):
    logger.debug("got called")
    try:
        notes_payload = json.dumps({
            "notes": request.POST.get('notes')
        })

        headers = {
            'Content-Type': 'application/json',
            'Accept':'application/json'
        }
        notes_response = requests.post(
            config('notes_endpoint'), 
            headers=headers, 
            data=notes_payload
        )

        if notes_response.status_code == 200:
            logger.debug("sending email success!")
            return True
        else:
            logger.debug("fa_wire_call email returned non-200 code.")
            return False

    except Exception as e:
        logger.debug("sending email returned an exception.")
        logger.debug(e)
        return