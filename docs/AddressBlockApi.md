# bloxoneipam.AddressBlockApi

All URIs are relative to *https://csp.infoblox.com/api/ddi/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**address_block_create**](AddressBlockApi.md#address_block_create) | **POST** /ipam/address_block | Create the Address Block object.
[**address_block_create_next_available_ip**](AddressBlockApi.md#address_block_create_next_available_ip) | **POST** /ipam/address_block/{id}/nextavailableip | Create the Next Available IP object.
[**address_block_delete**](AddressBlockApi.md#address_block_delete) | **DELETE** /ipam/address_block/{id} | Delete the Address Block object.
[**address_block_list**](AddressBlockApi.md#address_block_list) | **GET** /ipam/address_block | List Address Block objects.
[**address_block_list_next_available_ip**](AddressBlockApi.md#address_block_list_next_available_ip) | **GET** /ipam/address_block/{id}/nextavailableip | List Next Available IP objects.
[**address_block_read**](AddressBlockApi.md#address_block_read) | **GET** /ipam/address_block/{id} | Read the Address Block object.
[**address_block_update**](AddressBlockApi.md#address_block_update) | **PATCH** /ipam/address_block/{id} | Update the Address Block object.


# **address_block_create**
> IpamsvcCreateAddressBlockResponse address_block_create(body)

Create the Address Block object.

Use this method to create an Address Block object. The Address Block object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

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
api_instance = bloxoneipam.AddressBlockApi(bloxoneipam.ApiClient(configuration))
body = bloxoneipam.IpamsvcAddressBlock() # IpamsvcAddressBlock | 

try:
    # Create the Address Block object.
    api_response = api_instance.address_block_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressBlockApi->address_block_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpamsvcAddressBlock**](IpamsvcAddressBlock.md)|  | 

### Return type

[**IpamsvcCreateAddressBlockResponse**](IpamsvcCreateAddressBlockResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_block_create_next_available_ip**
> IpamsvcCreateNextAvailableIPResponse address_block_create_next_available_ip(id)

Create the Next Available IP object.

Use this method to create a Next Available IP object. The Next Available IP is a generator that allocates one or more ipam/address resource from available addresses when IP Address is not known prior to allocation.

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
api_instance = bloxoneipam.AddressBlockApi(bloxoneipam.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource

try:
    # Create the Next Available IP object.
    api_response = api_instance.address_block_create_next_available_ip(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressBlockApi->address_block_create_next_available_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 

### Return type

[**IpamsvcCreateNextAvailableIPResponse**](IpamsvcCreateNextAvailableIPResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_block_delete**
> address_block_delete(id)

Delete the Address Block object.

Use this method to delete an Address Block object. The Address Block object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

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
api_instance = bloxoneipam.AddressBlockApi(bloxoneipam.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource

try:
    # Delete the Address Block object.
    api_instance.address_block_delete(id)
except ApiException as e:
    print("Exception when calling AddressBlockApi->address_block_delete: %s\n" % e)
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

# **address_block_list**
> IpamsvcListAddressBlockResponse address_block_list(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, torder_by=torder_by, tfilter=tfilter)

List Address Block objects.

Use this method to list Address Block objects. The Address Block object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

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
api_instance = bloxoneipam.AddressBlockApi(bloxoneipam.ApiClient(configuration))
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)
offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
torder_by = 'torder_by_example' # str | This parameter is used for sorting by tags. (optional)
tfilter = 'tfilter_example' # str | This parameter is used for filtering by tags. (optional)

try:
    # List Address Block objects.
    api_response = api_instance.address_block_list(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, torder_by=torder_by, tfilter=tfilter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressBlockApi->address_block_list: %s\n" % e)
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

[**IpamsvcListAddressBlockResponse**](IpamsvcListAddressBlockResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_block_list_next_available_ip**
> IpamsvcNextAvailableIPResponse address_block_list_next_available_ip(id, contiguous=contiguous, count=count)

List Next Available IP objects.

Use this method to list Next Available IP objects. The Next Available IP is a generator that allocates one or more ipam/address resource from available addresses when IP Address is not known prior to allocation.

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
api_instance = bloxoneipam.AddressBlockApi(bloxoneipam.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
contiguous = true # bool |  (optional)
count = 56 # int |  (optional)

try:
    # List Next Available IP objects.
    api_response = api_instance.address_block_list_next_available_ip(id, contiguous=contiguous, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressBlockApi->address_block_list_next_available_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **contiguous** | **bool**|  | [optional] 
 **count** | **int**|  | [optional] 

### Return type

[**IpamsvcNextAvailableIPResponse**](IpamsvcNextAvailableIPResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_block_read**
> IpamsvcReadAddressBlockResponse address_block_read(id, fields=fields)

Read the Address Block object.

Use this method to read an Address Block object. The AddressBlock object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

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
api_instance = bloxoneipam.AddressBlockApi(bloxoneipam.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # Read the Address Block object.
    api_response = api_instance.address_block_read(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressBlockApi->address_block_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**IpamsvcReadAddressBlockResponse**](IpamsvcReadAddressBlockResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_block_update**
> IpamsvcUpdateAddressBlockResponse address_block_update(id, body)

Update the Address Block object.

Use this method to update an Address Block object. The Address Block object allows a uniform representation of the address space segmentation, supporting functions such as administrative grouping, routing aggregation, delegation etc.

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
api_instance = bloxoneipam.AddressBlockApi(bloxoneipam.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
body = bloxoneipam.IpamsvcAddressBlock() # IpamsvcAddressBlock | 

try:
    # Update the Address Block object.
    api_response = api_instance.address_block_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressBlockApi->address_block_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**IpamsvcAddressBlock**](IpamsvcAddressBlock.md)|  | 

### Return type

[**IpamsvcUpdateAddressBlockResponse**](IpamsvcUpdateAddressBlockResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

