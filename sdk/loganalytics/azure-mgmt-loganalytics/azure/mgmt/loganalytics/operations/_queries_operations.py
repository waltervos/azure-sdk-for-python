# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_request(
    subscription_id: str,
    resource_group_name: str,
    query_pack_name: str,
    *,
    top: Optional[int] = None,
    include_body: Optional[bool] = None,
    skip_token: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2019-09-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "queryPackName": _SERIALIZER.url("query_pack_name", query_pack_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if top is not None:
        query_parameters['$top'] = _SERIALIZER.query("top", top, 'long')
    if include_body is not None:
        query_parameters['includeBody'] = _SERIALIZER.query("include_body", include_body, 'bool')
    if skip_token is not None:
        query_parameters['$skipToken'] = _SERIALIZER.query("skip_token", skip_token, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_search_request(
    subscription_id: str,
    resource_group_name: str,
    query_pack_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    top: Optional[int] = None,
    include_body: Optional[bool] = None,
    skip_token: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2019-09-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries/search')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "queryPackName": _SERIALIZER.url("query_pack_name", query_pack_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if top is not None:
        query_parameters['$top'] = _SERIALIZER.query("top", top, 'long')
    if include_body is not None:
        query_parameters['includeBody'] = _SERIALIZER.query("include_body", include_body, 'bool')
    if skip_token is not None:
        query_parameters['$skipToken'] = _SERIALIZER.query("skip_token", skip_token, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_get_request(
    subscription_id: str,
    resource_group_name: str,
    query_pack_name: str,
    id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2019-09-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries/{id}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "queryPackName": _SERIALIZER.url("query_pack_name", query_pack_name, 'str'),
        "id": _SERIALIZER.url("id", id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_put_request(
    subscription_id: str,
    resource_group_name: str,
    query_pack_name: str,
    id: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2019-09-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries/{id}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "queryPackName": _SERIALIZER.url("query_pack_name", query_pack_name, 'str'),
        "id": _SERIALIZER.url("id", id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_update_request(
    subscription_id: str,
    resource_group_name: str,
    query_pack_name: str,
    id: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2019-09-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries/{id}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "queryPackName": _SERIALIZER.url("query_pack_name", query_pack_name, 'str'),
        "id": _SERIALIZER.url("id", id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PATCH",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_delete_request(
    subscription_id: str,
    resource_group_name: str,
    query_pack_name: str,
    id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2019-09-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries/{id}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "queryPackName": _SERIALIZER.url("query_pack_name", query_pack_name, 'str'),
        "id": _SERIALIZER.url("id", id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

class QueriesOperations(object):
    """QueriesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.loganalytics.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        query_pack_name: str,
        top: Optional[int] = None,
        include_body: Optional[bool] = None,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.LogAnalyticsQueryPackQueryListResult"]:
        """Gets a list of Queries defined within a Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource.
        :type query_pack_name: str
        :param top: Maximum items returned in page.
        :type top: long
        :param include_body: Flag indicating whether or not to return the body of each applicable
         query. If false, only return the query information.
        :type include_body: bool
        :param skip_token: Base64 encoded token used to fetch the next page of items. Default is null.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either LogAnalyticsQueryPackQueryListResult or the result
         of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQueryListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LogAnalyticsQueryPackQueryListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    query_pack_name=query_pack_name,
                    top=top,
                    include_body=include_body,
                    skip_token=skip_token,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    query_pack_name=query_pack_name,
                    top=top,
                    include_body=include_body,
                    skip_token=skip_token,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("LogAnalyticsQueryPackQueryListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries'}  # type: ignore

    @distributed_trace
    def search(
        self,
        resource_group_name: str,
        query_pack_name: str,
        query_search_properties: "_models.LogAnalyticsQueryPackQuerySearchProperties",
        top: Optional[int] = None,
        include_body: Optional[bool] = None,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.LogAnalyticsQueryPackQueryListResult"]:
        """Search a list of Queries defined within a Log Analytics QueryPack according to given search
        properties.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource.
        :type query_pack_name: str
        :param query_search_properties: Properties by which to search queries in the given Log
         Analytics QueryPack.
        :type query_search_properties:
         ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuerySearchProperties
        :param top: Maximum items returned in page.
        :type top: long
        :param include_body: Flag indicating whether or not to return the body of each applicable
         query. If false, only return the query information.
        :type include_body: bool
        :param skip_token: Base64 encoded token used to fetch the next page of items. Default is null.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either LogAnalyticsQueryPackQueryListResult or the result
         of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQueryListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LogAnalyticsQueryPackQueryListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                _json = self._serialize.body(query_search_properties, 'LogAnalyticsQueryPackQuerySearchProperties')
                
                request = build_search_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    query_pack_name=query_pack_name,
                    content_type=content_type,
                    json=_json,
                    top=top,
                    include_body=include_body,
                    skip_token=skip_token,
                    template_url=self.search.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                _json = self._serialize.body(query_search_properties, 'LogAnalyticsQueryPackQuerySearchProperties')
                
                request = build_search_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    query_pack_name=query_pack_name,
                    content_type=content_type,
                    json=_json,
                    top=top,
                    include_body=include_body,
                    skip_token=skip_token,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("LogAnalyticsQueryPackQueryListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    search.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries/search'}  # type: ignore

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        query_pack_name: str,
        id: str,
        **kwargs: Any
    ) -> "_models.LogAnalyticsQueryPackQuery":
        """Gets a specific Log Analytics Query defined within a Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource.
        :type query_pack_name: str
        :param id: The id of a specific query defined in the Log Analytics QueryPack.
        :type id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogAnalyticsQueryPackQuery, or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LogAnalyticsQueryPackQuery"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            query_pack_name=query_pack_name,
            id=id,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('LogAnalyticsQueryPackQuery', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries/{id}'}  # type: ignore


    @distributed_trace
    def put(
        self,
        resource_group_name: str,
        query_pack_name: str,
        id: str,
        query_payload: "_models.LogAnalyticsQueryPackQuery",
        **kwargs: Any
    ) -> "_models.LogAnalyticsQueryPackQuery":
        """Adds or Updates a specific Query within a Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource.
        :type query_pack_name: str
        :param id: The id of a specific query defined in the Log Analytics QueryPack.
        :type id: str
        :param query_payload: Properties that need to be specified to create a new query and add it to
         a Log Analytics QueryPack.
        :type query_payload: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogAnalyticsQueryPackQuery, or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LogAnalyticsQueryPackQuery"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(query_payload, 'LogAnalyticsQueryPackQuery')

        request = build_put_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            query_pack_name=query_pack_name,
            id=id,
            content_type=content_type,
            json=_json,
            template_url=self.put.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('LogAnalyticsQueryPackQuery', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries/{id}'}  # type: ignore


    @distributed_trace
    def update(
        self,
        resource_group_name: str,
        query_pack_name: str,
        id: str,
        query_payload: "_models.LogAnalyticsQueryPackQuery",
        **kwargs: Any
    ) -> "_models.LogAnalyticsQueryPackQuery":
        """Adds or Updates a specific Query within a Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource.
        :type query_pack_name: str
        :param id: The id of a specific query defined in the Log Analytics QueryPack.
        :type id: str
        :param query_payload: Properties that need to be specified to create a new query and add it to
         a Log Analytics QueryPack.
        :type query_payload: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogAnalyticsQueryPackQuery, or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.LogAnalyticsQueryPackQuery
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LogAnalyticsQueryPackQuery"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(query_payload, 'LogAnalyticsQueryPackQuery')

        request = build_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            query_pack_name=query_pack_name,
            id=id,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('LogAnalyticsQueryPackQuery', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries/{id}'}  # type: ignore


    @distributed_trace
    def delete(
        self,
        resource_group_name: str,
        query_pack_name: str,
        id: str,
        **kwargs: Any
    ) -> None:
        """Deletes a specific Query defined within an Log Analytics QueryPack.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param query_pack_name: The name of the Log Analytics QueryPack resource.
        :type query_pack_name: str
        :param id: The id of a specific query defined in the Log Analytics QueryPack.
        :type id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            query_pack_name=query_pack_name,
            id=id,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/queryPacks/{queryPackName}/queries/{id}'}  # type: ignore
