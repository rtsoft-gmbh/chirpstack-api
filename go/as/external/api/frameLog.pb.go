// Code generated by protoc-gen-go. DO NOT EDIT.
// source: as/external/api/frameLog.proto

package api

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	_ "github.com/golang/protobuf/ptypes/duration"
	timestamp "github.com/golang/protobuf/ptypes/timestamp"
	_ "github.com/rtsoft-gmbh/chirpstack-api/go/v3/common"
	gw "github.com/rtsoft-gmbh/chirpstack-api/go/v3/gw"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type RXWindow int32

const (
	RXWindow_RX1 RXWindow = 0
	RXWindow_RX2 RXWindow = 1
)

var RXWindow_name = map[int32]string{
	0: "RX1",
	1: "RX2",
}

var RXWindow_value = map[string]int32{
	"RX1": 0,
	"RX2": 1,
}

func (x RXWindow) String() string {
	return proto.EnumName(RXWindow_name, int32(x))
}

func (RXWindow) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_d215818867a60801, []int{0}
}

type UplinkFrameLog struct {
	// TX information of the uplink.
	TxInfo *gw.UplinkTXInfo `protobuf:"bytes,1,opt,name=tx_info,json=txInfo,proto3" json:"tx_info,omitempty"`
	// RX information of the uplink.
	RxInfo []*gw.UplinkRXInfo `protobuf:"bytes,2,rep,name=rx_info,json=rxInfo,proto3" json:"rx_info,omitempty"`
	// LoRaWAN PHYPayload.
	PhyPayloadJson string `protobuf:"bytes,3,opt,name=phy_payload_json,json=phyPayloadJSON,proto3" json:"phy_payload_json,omitempty"`
	// Published at timestamp.
	PublishedAt          *timestamp.Timestamp `protobuf:"bytes,4,opt,name=published_at,json=publishedAt,proto3" json:"published_at,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
}

func (m *UplinkFrameLog) Reset()         { *m = UplinkFrameLog{} }
func (m *UplinkFrameLog) String() string { return proto.CompactTextString(m) }
func (*UplinkFrameLog) ProtoMessage()    {}
func (*UplinkFrameLog) Descriptor() ([]byte, []int) {
	return fileDescriptor_d215818867a60801, []int{0}
}

func (m *UplinkFrameLog) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_UplinkFrameLog.Unmarshal(m, b)
}
func (m *UplinkFrameLog) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_UplinkFrameLog.Marshal(b, m, deterministic)
}
func (m *UplinkFrameLog) XXX_Merge(src proto.Message) {
	xxx_messageInfo_UplinkFrameLog.Merge(m, src)
}
func (m *UplinkFrameLog) XXX_Size() int {
	return xxx_messageInfo_UplinkFrameLog.Size(m)
}
func (m *UplinkFrameLog) XXX_DiscardUnknown() {
	xxx_messageInfo_UplinkFrameLog.DiscardUnknown(m)
}

var xxx_messageInfo_UplinkFrameLog proto.InternalMessageInfo

func (m *UplinkFrameLog) GetTxInfo() *gw.UplinkTXInfo {
	if m != nil {
		return m.TxInfo
	}
	return nil
}

func (m *UplinkFrameLog) GetRxInfo() []*gw.UplinkRXInfo {
	if m != nil {
		return m.RxInfo
	}
	return nil
}

func (m *UplinkFrameLog) GetPhyPayloadJson() string {
	if m != nil {
		return m.PhyPayloadJson
	}
	return ""
}

func (m *UplinkFrameLog) GetPublishedAt() *timestamp.Timestamp {
	if m != nil {
		return m.PublishedAt
	}
	return nil
}

type DownlinkFrameLog struct {
	// TX information of the downlink.
	TxInfo *gw.DownlinkTXInfo `protobuf:"bytes,1,opt,name=tx_info,json=txInfo,proto3" json:"tx_info,omitempty"`
	// LoRaWAN PHYPayload.
	PhyPayloadJson string `protobuf:"bytes,2,opt,name=phy_payload_json,json=phyPayloadJSON,proto3" json:"phy_payload_json,omitempty"`
	// Gateway ID.
	GatewayId string `protobuf:"bytes,3,opt,name=gateway_id,json=gatewayID,proto3" json:"gateway_id,omitempty"`
	// Published at timestamp.
	PublishedAt          *timestamp.Timestamp `protobuf:"bytes,4,opt,name=published_at,json=publishedAt,proto3" json:"published_at,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
}

func (m *DownlinkFrameLog) Reset()         { *m = DownlinkFrameLog{} }
func (m *DownlinkFrameLog) String() string { return proto.CompactTextString(m) }
func (*DownlinkFrameLog) ProtoMessage()    {}
func (*DownlinkFrameLog) Descriptor() ([]byte, []int) {
	return fileDescriptor_d215818867a60801, []int{1}
}

func (m *DownlinkFrameLog) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DownlinkFrameLog.Unmarshal(m, b)
}
func (m *DownlinkFrameLog) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DownlinkFrameLog.Marshal(b, m, deterministic)
}
func (m *DownlinkFrameLog) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DownlinkFrameLog.Merge(m, src)
}
func (m *DownlinkFrameLog) XXX_Size() int {
	return xxx_messageInfo_DownlinkFrameLog.Size(m)
}
func (m *DownlinkFrameLog) XXX_DiscardUnknown() {
	xxx_messageInfo_DownlinkFrameLog.DiscardUnknown(m)
}

var xxx_messageInfo_DownlinkFrameLog proto.InternalMessageInfo

func (m *DownlinkFrameLog) GetTxInfo() *gw.DownlinkTXInfo {
	if m != nil {
		return m.TxInfo
	}
	return nil
}

func (m *DownlinkFrameLog) GetPhyPayloadJson() string {
	if m != nil {
		return m.PhyPayloadJson
	}
	return ""
}

func (m *DownlinkFrameLog) GetGatewayId() string {
	if m != nil {
		return m.GatewayId
	}
	return ""
}

func (m *DownlinkFrameLog) GetPublishedAt() *timestamp.Timestamp {
	if m != nil {
		return m.PublishedAt
	}
	return nil
}

func init() {
	proto.RegisterEnum("api.RXWindow", RXWindow_name, RXWindow_value)
	proto.RegisterType((*UplinkFrameLog)(nil), "api.UplinkFrameLog")
	proto.RegisterType((*DownlinkFrameLog)(nil), "api.DownlinkFrameLog")
}

func init() {
	proto.RegisterFile("as/external/api/frameLog.proto", fileDescriptor_d215818867a60801)
}

var fileDescriptor_d215818867a60801 = []byte{
	// 397 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xa4, 0x92, 0x4f, 0x8f, 0xd3, 0x30,
	0x10, 0xc5, 0xc9, 0x06, 0xed, 0xb2, 0x2e, 0xac, 0xa2, 0x70, 0xa9, 0x2a, 0x58, 0x4a, 0x4f, 0x05,
	0x54, 0x5b, 0xb4, 0x47, 0xc4, 0x81, 0xaa, 0x42, 0x2a, 0x42, 0x50, 0x85, 0x22, 0x2a, 0x2e, 0x91,
	0xf3, 0xcf, 0x31, 0x4d, 0x3c, 0xc6, 0x71, 0x48, 0xf3, 0x09, 0x39, 0xf2, 0x95, 0x50, 0xea, 0x04,
	0xd4, 0xa8, 0xb7, 0x3d, 0x8d, 0xe7, 0xf9, 0x27, 0xfb, 0xbd, 0xd1, 0xa0, 0x5b, 0x5a, 0x90, 0xf8,
	0xa0, 0x63, 0x25, 0x68, 0x46, 0xa8, 0xe4, 0x24, 0x51, 0x34, 0x8f, 0x3f, 0x02, 0xc3, 0x52, 0x81,
	0x06, 0xd7, 0xa6, 0x92, 0x8f, 0x9e, 0x31, 0x00, 0x96, 0xc5, 0xe4, 0x28, 0x05, 0x65, 0x42, 0x34,
	0xcf, 0xe3, 0x42, 0xd3, 0x5c, 0x1a, 0x6a, 0x74, 0xdb, 0x07, 0xa2, 0x52, 0x51, 0xcd, 0x41, 0xb4,
	0xf7, 0x8f, 0x43, 0xc8, 0x73, 0x10, 0xc4, 0x94, 0x56, 0x1c, 0xb0, 0x8a, 0xb0, 0xca, 0x34, 0x93,
	0x3f, 0x16, 0xba, 0xf9, 0x2a, 0x33, 0x2e, 0xf6, 0xef, 0x5b, 0x03, 0xee, 0x0b, 0x74, 0xa5, 0x0f,
	0x3e, 0x17, 0x09, 0x0c, 0xad, 0xb1, 0x35, 0x1d, 0xcc, 0x1d, 0xcc, 0x2a, 0x6c, 0xa0, 0xed, 0x6e,
	0x2d, 0x12, 0xf0, 0x2e, 0xf5, 0xa1, 0xa9, 0x0d, 0xaa, 0x5a, 0xf4, 0x62, 0x6c, 0x9f, 0xa2, 0x5e,
	0x8b, 0x2a, 0x83, 0x4e, 0x91, 0x23, 0xd3, 0xda, 0x97, 0xb4, 0xce, 0x80, 0x46, 0xfe, 0x8f, 0x02,
	0xc4, 0xd0, 0x1e, 0x5b, 0xd3, 0x6b, 0xef, 0x46, 0xa6, 0xf5, 0xc6, 0xc8, 0x1f, 0xbe, 0x7c, 0xfe,
	0xe4, 0xbe, 0x45, 0x0f, 0x65, 0x19, 0x64, 0xbc, 0x48, 0xe3, 0xc8, 0xa7, 0x7a, 0x78, 0xff, 0x68,
	0x62, 0x84, 0x4d, 0x56, 0xdc, 0x65, 0xc5, 0xdb, 0x6e, 0x18, 0xde, 0xe0, 0x1f, 0xff, 0x4e, 0x4f,
	0x7e, 0x5b, 0xc8, 0x59, 0x41, 0x25, 0x4e, 0x32, 0xbd, 0xea, 0x67, 0x72, 0x1b, 0xa3, 0x1d, 0xd6,
	0x4b, 0x75, 0xce, 0xea, 0xc5, 0x59, 0xab, 0x4f, 0x11, 0x62, 0x54, 0xc7, 0x15, 0xad, 0x7d, 0x1e,
	0xb5, 0x71, 0xae, 0x5b, 0x65, 0xbd, 0xba, 0x63, 0x92, 0x97, 0x4f, 0xd0, 0x03, 0x6f, 0xf7, 0x8d,
	0x8b, 0x08, 0x2a, 0xf7, 0x0a, 0xd9, 0xde, 0xee, 0xb5, 0x73, 0xcf, 0x1c, 0xe6, 0x8e, 0xb5, 0xfc,
	0x89, 0x9e, 0x73, 0xc0, 0x61, 0xca, 0x95, 0x2c, 0x34, 0x0d, 0xf7, 0x98, 0x4a, 0x8e, 0x69, 0x81,
	0xbb, 0xad, 0x6a, 0xfa, 0xe5, 0xa3, 0x6e, 0x02, 0x9b, 0xe6, 0xaf, 0x8d, 0xf5, 0xfd, 0x0d, 0xe3,
	0x3a, 0x2d, 0x03, 0x1c, 0x42, 0x4e, 0x94, 0x2e, 0x20, 0xd1, 0x33, 0x96, 0x07, 0x29, 0xf9, 0xff,
	0xce, 0xac, 0xd9, 0x46, 0x06, 0xe4, 0xd7, 0x82, 0xf4, 0x76, 0x34, 0xb8, 0x3c, 0x3a, 0x5e, 0xfc,
	0x0d, 0x00, 0x00, 0xff, 0xff, 0x01, 0xe9, 0x25, 0x1e, 0xbd, 0x02, 0x00, 0x00,
}
