from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_tags_response_400_errors_item_payload import GetTagsResponse400ErrorsItemPayload


T = TypeVar("T", bound="GetTagsResponse400ErrorsItem")


@_attrs_define
class GetTagsResponse400ErrorsItem:
    """
    Attributes:
        key (Union[Unset, str]): Ключ параметра, в котором произошла ошибка.
        value (Union[Unset, str]): Значение ключа, вызвавшее ошибку.
        message (Union[Unset, str]): Текстовое описание ошибки.
        code (Union[Unset, str]): Внутренний код ошибки.
        payload (Union[Unset, GetTagsResponse400ErrorsItemPayload]): Дополнительная информация об ошибке.
    """

    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    payload: Union[Unset, "GetTagsResponse400ErrorsItemPayload"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        message = self.message

        code = self.code

        payload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if message is not UNSET:
            field_dict["message"] = message
        if code is not UNSET:
            field_dict["code"] = code
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_tags_response_400_errors_item_payload import GetTagsResponse400ErrorsItemPayload

        d = src_dict.copy()
        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        message = d.pop("message", UNSET)

        code = d.pop("code", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, GetTagsResponse400ErrorsItemPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = GetTagsResponse400ErrorsItemPayload.from_dict(_payload)

        get_tags_response_400_errors_item = cls(
            key=key,
            value=value,
            message=message,
            code=code,
            payload=payload,
        )

        get_tags_response_400_errors_item.additional_properties = d
        return get_tags_response_400_errors_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
