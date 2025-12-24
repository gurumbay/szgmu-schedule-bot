from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class Response(BaseModel):
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)


class ScheduleStatus(Response):
    """Schedule status model."""

    id: int
    name: str


class XlsxHeader(Response):
    """XLSX header information."""

    id: int
    lesson_type_name: str = Field(alias="lessonTypeName")
    semester_type: str = Field(alias="semesterType")
    academic_year: str = Field(alias="academicYear")
    course_number: str = Field(alias="courseNumber")
    speciality: str
    group_stream: str = Field(alias="groupStream")


class XlsxScheduleSummary(Response):
    """Summary of XLSX schedule."""

    id: int
    form_type: int = Field(alias="formType")
    file_name: str = Field(alias="fileName")
    xlsx_header_dto: list[XlsxHeader] = Field(alias="xlsxHeaderDto")
    schedule_status: ScheduleStatus = Field(alias="scheduleStatus")
    is_uploaded_from_xlsx: bool = Field(alias="isUploadedFromXlsx")


class ScheduleLesson(Response):
    """Detailed schedule lesson."""

    id: int
    subject_name: str = Field(alias="subjectName")
    pair_time: str = Field(alias="pairTime")
    department_name: str | None = Field(alias="departmentName")
    day_name: str = Field(alias="dayName")
    week_number: str = Field(alias="weekNumber")
    group_type_name: str | None = Field(alias="groupTypeName")
    lector_name: str | None = Field(alias="lectorName")
    auditory_number: str | None = Field(alias="auditoryNumber")
    location_address: str | None = Field(alias="locationAddress")
    study_group: str = Field(alias="studyGroup")
    subgroup: str = Field(alias="subgroup")
    group_stream: str = Field(alias="groupStream")
    schedule_id: int = Field(alias="scheduleId")
    file_name: str = Field(alias="fileName")
    lesson_type: str = Field(alias="lessonType")
    error_list: list[str] | None = Field(alias="errorList")
    speciality: str
    semester: str
    academic_year: str = Field(alias="academicYear")
    course_number: str = Field(alias="courseNumber")


class XlsxScheduleDetail(Response):
    """Detailed XLSX schedule."""

    id: int
    xlsx_header_dto: list[XlsxHeader] = Field(alias="xlsxHeaderDto")
    schedule_lesson_dto_list: list[ScheduleLesson] = Field(alias="scheduleLessonDtoList")
    subject_list: list[str] = Field(alias="subjectList")
    form_type: int = Field(alias="formType")
    status_id: int = Field(alias="statusId")
    file_name: str = Field(alias="fileName")
    is_uploaded_from_excel: bool = Field(alias="isUploadedFromExcel")
    update_time: datetime | None = Field(alias="updateTime")


class Pageable(Response):
    """Pagination information."""

    page_number: int = Field(alias="pageNumber")
    page_size: int = Field(alias="pageSize")
    sort: dict[str, bool] = Field(default_factory=dict)


class PaginatedResponse(Response):
    """Generic paginated response."""

    content: list[XlsxScheduleSummary]
    pageable: Pageable
    total_elements: int = Field(alias="totalElements")
    total_pages: int = Field(alias="totalPages")
    size: int
    number: int
    first: bool
    last: bool
    number_of_elements: int = Field(alias="numberOfElements")
    empty: bool
