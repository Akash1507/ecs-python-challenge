from marshmallow import Schema, fields
from marshmallow.validate import Range, Length


class CourseGetSchema(Schema):
    """
    Course Schema class to validate get input params.
    """

    page_number = fields.Integer(
        data_key="page-number",
        strict=False,
        validate=[Range(min=1, error="Value must be greater than 0")],
    )
    page_size = fields.Integer(
        data_key="page-size",
        strict=False,
        validate=[Range(min=1, error="Value must be greater than 0")],
    )
    title = fields.Str(required=False)


class CoursePostSchema(Schema):
    """
    Course Schema class to validate post data.
    """

    title = fields.Str(
        required=True,
        validate=[
            Length(
                min=5,
                max=100,
                error="Length of title must be between 5 and 100",
            )
        ],
    )
    description = fields.Str(
        required=False,
        validate=[
            Length(
                max=500,
                error="description should not exceed 255 characters",
            )
        ],
    )
    price = fields.Decimal(
        strict=True,
        required=True,
        validate=[Range(min=1, error="Value must be greater than 0")],
    )
    discount_price = fields.Decimal(
        strict=False, validate=[Range(min=1, error="Value must be greater than 0")]
    )
    image_path = fields.Str(
        required=False,
        validate=[
            Length(
                max=100,
                error="Length of image_path must be less than 100",
            )
        ],
    )
    on_discount = fields.Bool(strict=True, required=True)


class CoursePutSchema(Schema):
    """
    Course Schema class to validate put data.
    """

    id = fields.Integer(
        strict=False, validate=[Range(min=1, error="Value must be greater than 0")]
    )
    title = fields.Str(
        required=True,
        validate=[
            Length(
                min=5,
                max=100,
                error="Length of title must be between 5 and 100",
            )
        ],
    )
    description = fields.Str(
        required=False,
        validate=[
            Length(
                max=500,
                error="description should not exceed 255 characters",
            )
        ],
    )
    price = fields.Decimal(
        strict=True,
        required=True,
        validate=[Range(min=1, error="Value must be greater than 0")],
    )
    discount_price = fields.Decimal(
        strict=False, validate=[Range(min=1, error="Value must be greater than 0")]
    )
    image_path = fields.Str(
        required=False,
        validate=[
            Length(
                max=100,
                error="Length of image_path must be less than 100",
            )
        ],
    )
    on_discount = fields.Bool(strict=True, required=True)
    date_created = fields.DateTime(required=False)
    date_updated = fields.DateTime(required=False)