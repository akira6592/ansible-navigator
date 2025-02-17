"""A field with a 'working on it message'."""
from dataclasses import dataclass
from typing import Callable
from typing import List
from typing import Optional
from typing import Union

from .curses_window import Window
from .form_handler_working import FormHandlerWorking
from .sentinels import Unknown
from .sentinels import unknown
from .validators import FieldValidators


@dataclass
class FieldWorking:
    """A text input field."""

    name: str
    messages: List[str]
    current_error: str = ""
    window_handler = FormHandlerWorking
    valid: Union[bool, Unknown] = unknown
    validator: Callable = FieldValidators.null
    win: Optional[Window] = None

    @property
    def full_prompt(self) -> str:
        """Return the max width information.

        This is needed because windows width and : placement
        is based on the largest 'prompt'.

        :returns: Max width information message
        """
        return max(self.messages)

    def validate(self, response: str) -> None:
        # pylint: disable=unused-argument
        """No validation required for working field.

        :param response: Field response
        """
        self.valid = True

    def conditional_validation(self, response: str) -> None:
        """No conditional validation.

        :param response: Field response
        """
        self.validate(response)
