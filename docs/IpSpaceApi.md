# bloxoneipam.IpSpaceApi

All URIs are relative to *https://csp.infoblox.com/api/ddi/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ip_space_create**](IpSpaceApi.md#ip_space_create) | **POST** /ipam/ip_space | Create the IP Space object.
[**ip_space_delete**](IpSpaceApi.md#ip_space_delete) | **DELETE** /ipam/ip_space/{id} | Delete the IP Space object.
[**ip_space_list**](IpSpaceApi.md#ip_space_list) | **GET** /ipam/ip_space | List IP Space objects.
[**ip_space_read**](IpSpaceApi.md#ip_space_read) | **GET** /ipam/ip_space/{id} | Read the IP Space object.
[**ip_space_update**](IpSpaceApi.md#ip_space_update) | **PATCH** /ipam/ip_space/{id} | Update the IP Space object.


# **ip_space_create**
> IpamsvcCreateIPSpaceResponse ip_space_create(body)

Create the IP Space object.

Use this method to create an IP Space object. The IP Space object represents an entire address space.

### Example
```python
from __future__ import print_function
import time
import bloxoneipam
from bloxoneipam.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxoneipam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxoneipam.IpSpaceApi(bloxoneipam.ApiClient(configuration))
body = bloxoneipam.IpamsvcIPSpace() # IpamsvcIPSpace | 

try:
    # Create the IP Space object.
    api_response = api_instance.ip_space_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpSpaceApi->ip_space_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpamsvcIPSpace**](IpamsvcIPSpace.md)|  | 

### Return type

[**IpamsvcCreateIPSpaceResponse**](IpamsvcCreateIPSpaceResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_space_delete**
> ip_space_delete(id)

Delete the IP Space object.

Use this method to delete an IP Space object. The IP Space object represents an entire address space.

### Example
```python
from __future__ import print_function
import time
import bloxoneipam
from bloxoneipam.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxoneipam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxoneipam.IpSpaceApi(bloxoneipam.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource

try:
    # Delete the IP Space object.
    api_instance.ip_space_delete(id)
except ApiException as e:
    print("Exception when calling IpSpaceApi->ip_space_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_space_list**
> IpamsvcListIPSpaceResponse ip_space_list(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, torder_by=torder_by, tfilter=tfilter)

List IP Space objects.

Use this method to list IP Space objects. The IP Space object represents an entire address space.

### Example
```python
from __future__ import print_function
import time
import bloxoneipam
from bloxoneipam.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxoneipam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxoneipam.IpSpaceApi(bloxoneipam.ApiClient(configuration))
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)
offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
torder_by = 'torder_by_example' # str | This parameter is used for sorting by tags. (optional)
tfilter = 'tfilter_example' # str | This parameter is used for filtering by tags. (optional)

try:
    # List IP Space objects.
    api_response = api_instance.ip_space_list(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, torder_by=torder_by, tfilter=tfilter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpSpaceApi->ip_space_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **torder_by** | **str**| This parameter is used for sorting by tags. | [optional] 
 **tfilter** | **str**| This parameter is used for filtering by tags. | [optional] 

### Return type

[**IpamsvcListIPSpaceResponse**](IpamsvcListIPSpaceResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_space_read**
> IpamsvcReadIPSpaceResponse ip_space_read(id, fields=fields)

Read the IP Space object.

Use this method to read an IP Space object. The IP Space object represents an entire address space.

### Example
```python
from __future__ import print_function
import time
import bloxoneipam
from bloxoneipam.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxoneipam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxoneipam.IpSpaceApi(bloxoneipam.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # Read the IP Space object.
    api_response = api_instance.ip_space_read(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpSpaceApi->ip_space_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**IpamsvcReadIPSpaceResponse**](IpamsvcReadIPSpaceResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_space_update**
> IpamsvcUpdateIPSpaceResponse ip_space_update(id, body)

Update the IP Space object.

Use this method to update an IP Space object. The IP Space object represents an entire address space.

### Example
```python
from __future__ import print_function
import time
import bloxoneipam
from bloxoneipam.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxoneipam.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxoneipam.IpSpaceApi(bloxoneipam.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
body = bloxoneipam.IpamsvcIPSpace() # IpamsvcIPSpace | 

try:
    # Update the IP Space object.
    api_response = api_instance.ip_space_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpSpaceApi->ip_space_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**IpamsvcIPSpace**](IpamsvcIPSpace.md)|  | 

### Return type

[**IpamsvcUpdateIPSpaceResponse**](IpamsvcUpdateIPSpaceResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

