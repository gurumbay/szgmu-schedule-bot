from pydantic import BaseModel, ConfigDict, Field


class ScheduleFilters(BaseModel):
    """Filters for schedule search."""

    group_stream: list[str] = Field(default_factory=list, alias="groupStream")
    speciality: list[str] = Field(default_factory=list)
    lesson_type: list[str] = Field(default_factory=list, alias="lessonType")
    course_number: list[str] = Field(default_factory=list, alias="courseNumber")
    academic_year: list[str] = Field(default_factory=list, alias="academicYear")
    semester: list[str] = Field(default_factory=list)

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
