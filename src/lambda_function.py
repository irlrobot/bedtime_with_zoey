"""
Bedtime with Zoey Alexa Skill
Josh Campbell
"""

import logging
import brown_bear
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
sb = SkillBuilder()

@sb.global_request_interceptor()
def request_logger(handler_input):
    logger.debug("Envelope: {}".format(
        handler_input.request_envelope.request))
    logger.debug("Session: {}".format(
        handler_input.attributes_manager.session_attributes))

@sb.global_response_interceptor()
def response_logger(_handler_input, response):
    logger.debug("Response: {}".format(response))

@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
def launch_request_handler(handler_input):
    # type: (HandlerInput) -> Response
    speech_text = brown_bear.STORY

    handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard(
            "Bedtime with Zoey", speech_text
        )
    ).set_should_end_session(True)

    return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_intent_name("BrownBearStoryIntent"))
def brown_bear_story_intent_handler(handler_input):
    # type: (HandlerInput) -> Response
    speech_text = brown_bear.STORY

    handler_input.response_builder.speak(speech_text).set_card(
        SimpleCard(
            "Brown Bear, Brown Bear", speech_text
        )
    ).set_should_end_session(True)

    return handler_input.response_builder.response

handler = sb.lambda_handler()
