from typing import Dict, Any, Optional
import re
from dataclasses import dataclass

@dataclass
class ValidationResult:
    """Represents the result of trend context validation."""
    is_valid: bool
    errors: list[str]
    sanitized_data: Optional[Dict[str, Any]] = None

class TrendContextValidator:
    """
    Validates and sanitizes trend context data for crypto content generation.
    
    Provides comprehensive validation and sanitization of trend-related inputs,
    ensuring data integrity and preventing potential security risks.
    """
    
    @staticmethod
    def validate_trend_context(trend_context: Dict[str, Any]) -> ValidationResult:
        """
        Validate and sanitize the entire trend context.
        
        Args:
            trend_context (Dict[str, Any]): The trend context to validate
        
        Returns:
            ValidationResult: Validation result with errors and sanitized data
        """
        errors = []
        sanitized_data = {}
        
        # Validate and sanitize key trend context fields
        fields_to_validate = [
            'topic', 
            'source', 
            'relevance_score', 
            'market_sentiment'
        ]
        
        for field in fields_to_validate:
            if field not in trend_context:
                errors.append(f"Missing required field: {field}")
                continue
            
            # Field-specific validation methods
            validator_method = getattr(TrendContextValidator, f'_validate_{field}', None)
            if validator_method:
                validation_result = validator_method(trend_context[field])
                if not validation_result.is_valid:
                    errors.extend(validation_result.errors)
                else:
                    sanitized_data[field] = validation_result.sanitized_data
        
        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            sanitized_data=sanitized_data if errors == [] else None
        )
    
    @staticmethod
    def _validate_topic(topic: str) -> ValidationResult:
        """
        Validate and sanitize trend topic.
        
        Args:
            topic (str): Topic to validate
        
        Returns:
            ValidationResult: Validation result
        """
        if not isinstance(topic, str):
            return ValidationResult(
                is_valid=False, 
                errors=["Topic must be a string"]
            )
        
        # Sanitize topic: remove extra whitespaces, limit length
        sanitized_topic = re.sub(r'\s+', ' ', topic).strip()
        
        if len(sanitized_topic) < 2:
            return ValidationResult(
                is_valid=False, 
                errors=["Topic must be at least 2 characters long"]
            )
        
        if len(sanitized_topic) > 100:
            return ValidationResult(
                is_valid=False, 
                errors=["Topic must not exceed 100 characters"]
            )
        
        # Additional security: remove potential script tags or HTML
        sanitized_topic = re.sub(r'<[^>]+>', '', sanitized_topic)
        
        return ValidationResult(
            is_valid=True, 
            sanitized_data=sanitized_topic,
            errors=[]
        )
    
    @staticmethod
    def _validate_source(source: str) -> ValidationResult:
        """
        Validate and sanitize trend source.
        
        Args:
            source (str): Source to validate
        
        Returns:
            ValidationResult: Validation result
        """
        if not isinstance(source, str):
            return ValidationResult(
                is_valid=False, 
                errors=["Source must be a string"]
            )
        
        # Sanitize source: remove extra whitespaces
        sanitized_source = re.sub(r'\s+', ' ', source).strip()
        
        if len(sanitized_source) < 2:
            return ValidationResult(
                is_valid=False, 
                errors=["Source must be at least 2 characters long"]
            )
        
        if len(sanitized_source) > 50:
            return ValidationResult(
                is_valid=False, 
                errors=["Source must not exceed 50 characters"]
            )
        
        return ValidationResult(
            is_valid=True, 
            sanitized_data=sanitized_source,
            errors=[]
        )
    
    @staticmethod
    def _validate_relevance_score(score: float) -> ValidationResult:
        """
        Validate relevance score.
        
        Args:
            score (float): Relevance score to validate
        
        Returns:
            ValidationResult: Validation result
        """
        if not isinstance(score, (int, float)):
            return ValidationResult(
                is_valid=False, 
                errors=["Relevance score must be a number"]
            )
        
        try:
            sanitized_score = float(score)
            
            if sanitized_score < 0 or sanitized_score > 100:
                return ValidationResult(
                    is_valid=False, 
                    errors=["Relevance score must be between 0 and 100"]
                )
            
            return ValidationResult(
                is_valid=True, 
                sanitized_data=round(sanitized_score, 2),
                errors=[]
            )
        except (TypeError, ValueError):
            return ValidationResult(
                is_valid=False, 
                errors=["Invalid relevance score"]
            )
    
    @staticmethod
    def _validate_market_sentiment(sentiment: str) -> ValidationResult:
        """
        Validate market sentiment.
        
        Args:
            sentiment (str): Market sentiment to validate
        
        Returns:
            ValidationResult: Validation result
        """
        valid_sentiments = ['bullish', 'bearish', 'neutral']
        
        if not isinstance(sentiment, str):
            return ValidationResult(
                is_valid=False, 
                errors=["Market sentiment must be a string"]
            )
        
        sanitized_sentiment = sentiment.lower().strip()
        
        if sanitized_sentiment not in valid_sentiments:
            return ValidationResult(
                is_valid=False, 
                errors=[f"Invalid market sentiment. Must be one of: {', '.join(valid_sentiments)}"]
            )
        
        return ValidationResult(
            is_valid=True, 
            sanitized_data=sanitized_sentiment,
            errors=[]
        )