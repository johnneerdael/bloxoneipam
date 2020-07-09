# bloxoneipam.GlobalApi

All URIs are relative to *https://csp.infoblox.com/api/ddi/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**global_read**](GlobalApi.md#global_read) | **GET** /dhcp/global | Read the Global configuration object.
[**global_read2**](GlobalApi.md#global_read2) | **GET** /dhcp/global/{id} | Read the Global configuration object.
[**global_update**](GlobalApi.md#global_update) | **PATCH** /dhcp/global | Update the Global configuration object.
[**global_update2**](GlobalApi.md#global_update2) | **PATCH** /dhcp/global/{id} | Update the Global configuration object.


# **global_read**
> IpamsvcReadGlobalResponse global_read(fields=fields)

Read the Global configuration object.

Use this method to read the Global configuration object. Service operates on Global singleton object that represents parent configuration settings for inheritance.

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
api_instance = bloxoneipam.GlobalApi(bloxoneipam.ApiClient(configuration))
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # Read the Global configuration object.
    api_response = api_instance.global_read(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalApi->global_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**IpamsvcReadGlobalResponse**](IpamsvcReadGlobalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_read2**
> IpamsvcReadGlobalResponse global_read2(id, fields=fields)

Read the Global configuration object.

Use this method to read the Global configuration object. Service operates on Global singleton object that represents parent configuration settings for inheritance.

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
api_instance = bloxoneipam.GlobalApi(bloxoneipam.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # Read the Global configuration object.
    api_response = api_instance.global_read2(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalApi->global_read2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**IpamsvcReadGlobalResponse**](IpamsvcReadGlobalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_update**
> IpamsvcUpdateGlobalResponse global_update(body)

Update the Global configuration object.

Use this method to update the Global configuration object. Service operates on Global singleton object that represents parent configuration settings for inheritance.

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
api_instance = bloxoneipam.GlobalApi(bloxoneipam.ApiClient(configuration))
body = bloxoneipam.IpamsvcGlobal() # IpamsvcGlobal | 

try:
    # Update the Global configuration object.
    api_response = api_instance.global_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalApi->global_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpamsvcGlobal**](IpamsvcGlobal.md)|  | 

### Return type

[**IpamsvcUpdateGlobalResponse**](IpamsvcUpdateGlobalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_update2**
> IpamsvcUpdateGlobalResponse global_update2(id, body)

Update the Global configuration object.

Use this method to update the Global configuration object. Service operates on Global singleton object that represents parent configuration settings for inheritance.

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
api_instance = bloxoneipam.GlobalApi(bloxoneipam.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
body = bloxoneipam.IpamsvcGlobal() # IpamsvcGlobal | 

try:
    # Update the Global configuration object.
    api_response = api_instance.global_update2(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalApi->global_update2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**IpamsvcGlobal**](IpamsvcGlobal.md)|  | 

### Return type

[**IpamsvcUpdateGlobalResponse**](IpamsvcUpdateGlobalResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

