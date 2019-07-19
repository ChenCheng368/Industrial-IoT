# encoding: utf-8
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module azure.iiot.opc.registry
  module Models
    #
    # List of registered applications
    #
    class ApplicationInfoListApiModel
      # @return [Array<ApplicationInfoApiModel>] Application infos
      attr_accessor :items

      # @return [String] Continuation or null if final
      attr_accessor :continuation_token


      #
      # Mapper for ApplicationInfoListApiModel class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          client_side_validation: true,
          required: false,
          serialized_name: 'ApplicationInfoListApiModel',
          type: {
            name: 'Composite',
            class_name: 'ApplicationInfoListApiModel',
            model_properties: {
              items: {
                client_side_validation: true,
                required: false,
                serialized_name: 'items',
                type: {
                  name: 'Sequence',
                  element: {
                      client_side_validation: true,
                      required: false,
                      serialized_name: 'ApplicationInfoApiModelElementType',
                      type: {
                        name: 'Composite',
                        class_name: 'ApplicationInfoApiModel'
                      }
                  }
                }
              },
              continuation_token: {
                client_side_validation: true,
                required: false,
                serialized_name: 'continuationToken',
                type: {
                  name: 'String'
                }
              }
            }
          }
        }
      end
    end
  end
end
