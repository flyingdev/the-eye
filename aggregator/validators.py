def validate_format(payload) -> bool:
    if not payload.get('session_id'):
        return False

    if not payload.get('category'):
        return False

    if not payload.get('name'):
        return False

    if not payload.get('data'):
        return False

    if not payload.get('timestamp'):
        return False

    return True


class ValidatorFactory:
    def __init__(self):
        self._builders = {}

    def register_validator(self, key, validator):
        self._builders[key] = validator

    def validate(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)

        return builder(**kwargs)


def validate_page_interaction_cta_click(data) -> bool:
    if not data.get('host'):
        return False
    if not data.get('path'):
        return False
    if not data.get('element'):
        return False

    return True


validator_factory = ValidatorFactory()
validator_factory.register_validator('page interaction cta click', validate_page_interaction_cta_click)
