from dataclasses import dataclass
from enum import Enum


class ScheduleEndpoint:
    """Schedule-related API endpoints."""

    @staticmethod
    def find_all(page: int = 0) -> str:
        """Get endpoint for finding all schedules."""
        return f"xlsxSchedule/findAll/{page}"

    @staticmethod
    def find_by_id() -> str:
        """Get endpoint for finding schedule by ID."""
        return "xlsxSchedule/findById"


class FilterType(str, Enum):
    """Available filter types."""

    GROUP_STREAM = "groupStream"
    SPECIALITY = "speciality"
    LESSON_TYPE = "lessonType"
    COURSE_NUMBER = "courseNumber"
    ACADEMIC_YEAR = "academicYear"
    SEMESTER = "semester"


@dataclass
class APIConfig:
    """API configuration."""

    base_url: str = "https://frsview.szgmu.ru/api"
    timeout: int = 30
    max_retries: int = 3
    enable_cache: bool = True
    cache_ttl: int = 300  # 5 minutes
