from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class ScheduleStatus(BaseModel):
    id: int
    name: str


class XlsxHeader(BaseModel):
    id: int
    lesson_type_name: str = Field(alias="lessonTypeName")
    semester_type: str = Field(alias="semesterType")
    academic_year: str = Field(alias="academicYear")
    course_number: str = Field(alias="courseNumber")
    speciality: str
    group_stream: str = Field(alias="groupStream")


class XlsxScheduleSummary(BaseModel):
    id: int
    form_type: int = Field(alias="formType")
    file_name: str = Field(alias="fileName")
    xlsx_header_dto: List[XlsxHeader] = Field(alias="xlsxHeaderDto")
    schedule_status: ScheduleStatus = Field(alias="scheduleStatus")
    is_uploaded_from_xlsx: bool = Field(alias="isUploadedFromXlsx")


class PaginatedResponse(BaseModel):
    content: List[XlsxScheduleSummary]
    total_elements: int = Field(alias="totalElements")
    total_pages: int = Field(alias="totalPages")
    size: int
    number: int
    first: bool
    last: bool
    number_of_elements: int = Field(alias="numberOfElements")
    empty: bool


class ScheduleLesson(BaseModel):
    id: int
    subject_name: str = Field(alias="subjectName")
    pair_time: str = Field(alias="pairTime")
    department_name: Optional[str] = Field(alias="departmentName")
    day_name: str = Field(alias="dayName")
    week_number: str = Field(alias="weekNumber")
    group_type_name: Optional[str] = Field(alias="groupTypeName")
    lector_name: Optional[str] = Field(alias="lectorName")
    auditory_number: Optional[str] = Field(alias="auditoryNumber")
    location_address: Optional[str] = Field(alias="locationAddress")
    study_group: str = Field(alias="studyGroup")
    subgroup: str
    group_stream: str = Field(alias="groupStream")
    schedule_id: int = Field(alias="scheduleId")
    file_name: str = Field(alias="fileName")
    lesson_type: str = Field(alias="lessonType")
    error_list: Optional[List[str]] = Field(alias="errorList")
    speciality: str
    semester: str
    academic_year: str = Field(alias="academicYear")
    course_number: str = Field(alias="courseNumber")


class ScheduleDetails(BaseModel):
    id: int
    xlsx_header_dto: List[XlsxHeader] = Field(alias="xlsxHeaderDto")
    schedule_lesson_dto_list: List[ScheduleLesson] = Field(alias="scheduleLessonDtoList")
    subject_list: List[str] = Field(alias="subjectList")
    form_type: int = Field(alias="formType")
    status_id: int = Field(alias="statusId")
    file_name: str = Field(alias="fileName")
    is_uploaded_from_excel: bool = Field(alias="isUploadedFromExcel")
    update_time: Optional[datetime] = Field(alias="updateTime")


# Request schemas
class FilterRequest(BaseModel):
    group_stream: List[str] = Field(default_factory=list, alias="groupStream")
    speciality: List[str] = Field(default_factory=list)
    lesson_type: List[str] = Field(default_factory=list, alias="lessonType")
    course_number: List[str] = Field(default_factory=list, alias="courseNumber")
    academic_year: List[str] = Field(default_factory=list, alias="academicYear")
    semester: List[str] = Field(default_factory=list)
