// <auto-generated>
// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
//
// Code generated by Microsoft (R) AutoRest Code Generator 1.0.0.0
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace Microsoft.Azure.IIoT.Opc.Twin.Models
{
    using Newtonsoft.Json;
    using System.Collections;
    using System.Collections.Generic;
    using System.Linq;

    /// <summary>
    /// Method call response model
    /// </summary>
    public partial class MethodCallResponseApiModel
    {
        /// <summary>
        /// Initializes a new instance of the MethodCallResponseApiModel class.
        /// </summary>
        public MethodCallResponseApiModel()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the MethodCallResponseApiModel class.
        /// </summary>
        /// <param name="results">Output results</param>
        /// <param name="errorInfo">Service result in case of error</param>
        public MethodCallResponseApiModel(IList<MethodCallArgumentApiModel> results = default(IList<MethodCallArgumentApiModel>), ServiceResultApiModel errorInfo = default(ServiceResultApiModel))
        {
            Results = results;
            ErrorInfo = errorInfo;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets or sets output results
        /// </summary>
        [JsonProperty(PropertyName = "results")]
        public IList<MethodCallArgumentApiModel> Results { get; set; }

        /// <summary>
        /// Gets or sets service result in case of error
        /// </summary>
        [JsonProperty(PropertyName = "errorInfo")]
        public ServiceResultApiModel ErrorInfo { get; set; }

    }
}
